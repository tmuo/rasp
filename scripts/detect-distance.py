# %%

import cv2
import pyrealsense2
from realsense_depth import * # Import everything

from sklearn.preprocessing import MinMaxScaler

# %%

point = (400, 300) # Starting location of pointer

def show_distance(event, x, y, args, params):
    global point # Follows the mouse location
    point = (x, y)

# %%

# Initialize Camera Intel Realsense
dc = DepthCamera()

# Create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

i = 0

while True:
    ret, depth_frame, color_frame = dc.get_frame(dec=False, spat=False, temp=False)

    #print(f'Depth scale: {depth_scale}')

    # Create a scaler for the depth data
    if (i % 90 == 0):  
        scaler = MinMaxScaler(feature_range=(0, 255))
        scaler.partial_fit(depth_frame)
    else:
        pass

    # Show distance for a specific point
    cv2.circle(color_frame, point, 4, (0, 0, 255))
    distance = depth_frame[point[1], point[0]] # First y, second x

    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    #cv2.imshow("Depth frame", cv2.medianBlur(cv2.applyColorMap(scaler.transform(depth_frame).astype('uint8'), cv2.COLORMAP_JET), 5))
    #cv2.imshow("Depth frame", cv2.applyColorMap(scaler.transform(depth_frame).astype('uint8'), cv2.COLORMAP_JET))
    cv2.imshow("Depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
    key = cv2.waitKey(1)

    if key == 27:
        cv2. destroyAllWindows()
        break
        

    i += 0

    if i == 900:
        i = 0
    else:
        pass


# %%
