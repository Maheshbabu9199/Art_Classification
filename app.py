from prediction import predict, load_custom_model
import streamlit as st 



def main():
    load_custom_model()
    st.title('Art Classification App')
    st.subheader('Upload an image of an art piece')


    image_file = st.file_uploader('Upload Art Image', type=['jpg', 'png', 'jpeg'])

    if image_file is not None:
        st.image(image_file)

        if st.button('Predict'):
            if image_file is not None:
                result = predict(image_file)
                if result == 'Ai':
                    result = 'AI Art'
                    st.warning(result)
                else:
                    result = 'Real Art'
                    st.success(result)
    else:
        st.info('Please upload an image file')


if __name__ == '__main__':
    main()
