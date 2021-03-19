import streamlit as st
from PIL import Image
import style
import io
import os

st.title('Pytorch Style Transfer')

input_image = st.file_uploader('Upload Image:')
input_image_path = ''
if input_image is not None:
    input_image_path = 'neural_style/images/content-images/'+input_image.name


st.write('### Source Image:')
if input_image is not None:
    with open(os.path.join("neural_style/images/content-images/",input_image.name),"wb") as f: 
        f.write(input_image.getbuffer())
    img = Image.open(input_image)
    st.image(img,width=250)

if input_image:
    st.write(input_image.name)

style_name = st.selectbox(
  'Select Style',
  ('candy', 'mosaic', 'rain_princess', 'udnie')
)

model = 'neural_style/saved_models/'+style_name+'.pth'
if input_image is not None:
    output_image = 'neural_style/images/output-images/'+style_name+'-'+input_image.name
clicked = st.button('Stylize')

if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image_path, output_image)

    st.write('### Stylized Image:')
    image = Image.open(output_image)
    st.image(image, width=400)