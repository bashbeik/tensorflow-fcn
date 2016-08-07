#!/usr/bin/env python

import skimage
import skimage.io
import skimage.transform

import os
import scipy as scp
import scipy.misc

import numpy as np
import logging
import tensorflow as tf
import sys

import fcn8_vgg
import utils

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)

from tensorflow.python.framework import ops

os.environ['CUDA_VISIBLE_DEVICES'] = ''
vgg_fcn = fcn8_vgg.FCN8VGG()
img1 = skimage.io.imread("./test_data/img.jpg")
images = tf.placeholder("float")
feed_dict = {images: img1}
batch_images = tf.expand_dims(images, 0)
with tf.name_scope("content_vgg"):
    vgg_fcn.build(batch_images, debug=True)


print('Finished building Network.')

saver = tf.train.Saver()
with tf.Session() as sess:
    

		    
		    
    saver.restore(sess, "./train (copy)/comment-19000")
    logging.warning("Score weights are initialized random.")
    logging.warning("Do not expect meaningful results.")

    logging.info("Start Initializing Variabels.")

    #init = tf.initialize_all_variables()
    #sess.run(tf.initialize_all_variables())

    print('Running the Network')
    tensors = [vgg_fcn.pred, vgg_fcn.pred_up]
    down, up = sess.run(tensors, feed_dict=feed_dict)

    down_color = utils.color_image(down[0])
    up_color = utils.color_image(up[0])

    scp.misc.imsave('fcn8_downsampled.png', down_color)
    scp.misc.imsave('fcn8_upsampled.png', up_color)
