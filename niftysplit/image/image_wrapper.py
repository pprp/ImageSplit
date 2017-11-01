# coding=utf-8
"""A wrapper for a multi-dimensional image with an origin offset"""

import numpy as np


class ImageWrapper(object):
    """Mult-dimensional image array with an origin"""

    def __init__(self, origin, image_size=None, image=None):
        self.origin = origin
        if image is not None:
            self.size = list(image.shape)
        else:
            self.size = image_size
        self.image = image

    def set_sub_image(self, sub_image):
        """Replaces part of the image with the corresponding subimage"""
        if self.image is None:
            self.image = np.zeros(shape=self.size, dtype=sub_image.image.dtype)
        start_indices = np.subtract(sub_image.origin, self.origin)
        end_indices = np.add(start_indices, np.array(sub_image.size))
        if np.any(np.less(start_indices,
                          np.zeros(shape=start_indices.shape))) \
                or np.any(np.greater(end_indices, self.size)):
            raise ValueError("Subimage is not contained within the main image")
        selector = tuple([slice(start, end) for start, end in
                          zip(start_indices, end_indices)])
        self.image[selector] = sub_image.image