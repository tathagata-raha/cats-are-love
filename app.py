from connection import CatConnection
import streamlit as st
from requests import get
from PIL import Image
from io import BytesIO

def main():
    connection = CatConnection()
    st.title('Cats are Love!')
    st.markdown('Check the supported tags [here](https://cataas.com/api/tags).')

    tag = st.text_input('Tag:', '')
    says = st.text_input('Says:', '')
    img = None
    if st.button('Enter'):
        if tag == '':
            st.write('Please enter a tag to search for a cat.')
        else:
            if says == "":
                img = connection.query(tag=tag)
            else:
                img = connection.query(tag=tag, says=says)
            st.write(f'You searched for the cat with tag: {tag}')
            st.write(f'You want the cat to say: {says}')

    if st.button('Random'):
        img = connection.randon_query()
        st.write('You clicked the Random button.')

    if img:
        img = Image.open(BytesIO(img))
        st.image(img, caption="Your image",  use_column_width=True)

if __name__ == "__main__":
    main()