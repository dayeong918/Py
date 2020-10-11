import streamlit as st
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image

st.set_option('deprecation.showfileUploaderEncoding', False)
# functions
def img_scaler(image, max_dim = 512):

  # Casts a tensor to a new type.
  original_shape = tf.cast(tf.shape(image)[:-1], tf.float32)

  # Creates a scale constant for the image
  scale_ratio = max_dim / max(original_shape)

  # Casts a tensor to a new type.
  new_shape = tf.cast(original_shape * scale_ratio, tf.int32)

  # Resizes the image based on the scaling constant generated above
  return tf.image.resize(image, new_shape)


#### Load images
# Types of images
imgTypes = ["png", "jpg"]

st.info("Upload source image on Streamlit")
source_img_buf = st.file_uploader("Upload source image", type=imgTypes, key='src')

if source_img_buf is not None:
    source_img = Image.open(source_img_buf)
    st.success("Source image uploaded!")

st.info("Upload style image on Streamlit")
style_img_buf = st.file_uploader("Upload style image", type=imgTypes, key='style')
if style_img_buf is not None:
    style_img = Image.open(style_img_buf)
    st.success("Style image uploaded!")

st.info("Check here to see source and style images:")
if st.checkbox("Show source and style images", key='raw'):
  fig = plt.figure(figsize=(12, 6))
  plt.subplot(1, 2, 1)
  plt.imshow(source_img)
  plt.title('Source Image')
  plt.subplot(1, 2, 2)
  plt.imshow(style_img)
  plt.title('Style Image')
  st.pyplot(fig)


st.info("Check here to compare three images:source, style, target")
if st.checkbox("Show source and style images", key='compare'):
  fig = plt.figure(figsize=(12, 6))
  plt.subplot(1, 3, 1)
  plt.imshow(source_img)
  plt.title('Source Image')
  plt.subplot(1, 3, 2)
  plt.imshow(style_img)
  plt.title('Style Image')
  plt.subplot(1, 3, 3)
  plt.imshow(style_img)
  plt.title('Styled Image')
  st.pyplot(fig)
  st.success("Completed!")




