import argparse
from cam_motion_field import get_cam_flow
import cv2
import numpy as np


def parseargs():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='''compute the camera motion optical flow between two images.''')
    parser.add_argument('--images', '-i', nargs=2, type=str, help="path to the two image files")
    parser.add_argument(
        "--grid-size",
        "-g",
        nargs="+",
        type=int,
        help="A touple representing the nrows and ncols of the grid.",
    )
    args = parser.parse_args()
    return args


def render_displacements(frame, origins, displacements, magnification = 1):
    """ Render small vector lines on the image representing the optical flow.

    Parameters
    ----------
    frame: numpy array,
        Array representing the RGB frame.
    origins: numpy array,
        Array representing the origin of each grid point.
    displacements: numpy array,
        Array representing the displacements of each grid point.

    Returns
    -------
        The image as an RBG numpy array with the rendered lines.
    """
    out_frame = np.array(frame)
    for v0, v1 in zip(np.reshape(origins, (-1, 2)), np.reshape(displacements, (-1, 2))):
        v1 = (v1-v0)*magnification+v0
        out_frame = cv2.arrowedLine(out_frame, tuple(v0), tuple(v1), (0, 255, 0), thickness=1)
    return out_frame


def main(images, grid_size):
    img1 = cv2.imread(images[0], 0)
    img2 = cv2.imread(images[1], 0)
    origins, displacements = get_cam_flow(img1, img2, grid_size[0], grid_size[1])
    motion_field = render_displacements(np.ones_like(img2)*255, origins, displacements, magnification=1)
    cv2.imwrite("motion_filed_{}x{}.jpg".format(*grid_size), motion_field)

if __name__ == "__main__":
    args = parseargs()
    main(**args.__dict__)
