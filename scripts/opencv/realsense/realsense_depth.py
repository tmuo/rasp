import pyrealsense2.pyrealsense2 as rs
import numpy as np

class DepthCamera:
    def __init__(self):
        # Configure depth and color streams
        self.pipeline = rs.pipeline()
        config = rs.config()

        # Get device product line for setting a supporting resolution
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device().first_depth_sensor()
        depth_scale = device.get_depth_scale() # Should have scaling
        device_product_line = str(device.get_info(rs.camera_info.product_line))

        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

        # Start streaming
        self.pipeline.start(config)

    def get_frame(self, dec=False, spat=False, temp=False):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        
        dec_filter = rs.decimation_filter()   # Decimation - reduces depth frame density
        spat_filter = rs.spatial_filter()     # Spatial    - edge-preserving spatial smoothing
        temp_filter = rs.temporal_filter()    # Temporal   - reduces temporal noise

        if dec:
            depth_image = dec_filter.process(depth_image)
        if spat:
            depth_image = spat_filter.process(depth_image)
        if temp:
            depth_image = temp_filter.process(depth_image)

        if not depth_frame or not color_frame:
            return False, None, None
        return True, depth_image, color_image

    def release(self):
        self.pipeline.stop()
