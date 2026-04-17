import streamlit as st
from PIL import Image
from api_call import issue_founder, Hints_Only, Fixed_code

st.title("AI Code Debugger", anchor = False)
st.subheader("Upload the image of your code error")
st.divider()

with st.sidebar:
    st.header("Controls")

    images = st.file_uploader("Upload the photo of your code", ['jpg','jpeg','png'])
    if images:
        pil_image =  Image.open(images)
        st.image(pil_image)


    st.subheader("How do you want to solve the problem")

    select= st.selectbox("Choose an option",("Hints Only","Solution With Code"), index = None)
    pressed = st.button("Click the button to initiate AI", type= "primary")

if pressed:
    if not images:
        st.error("Upload the image of code error")
    if not select:
        st.error("you have to select an option")
    
    if images and select:
        with st.container(border=True):
            st.subheader("The Issue")
            with st.spinner("AI is finding issue of your code"):
                found_issue = issue_founder(pil_image)
                st.markdown(found_issue)

        
        with st.container(border=True):
            st.subheader(f"Solution ({select})")
            
            if select == "Hints Only":
                with st.spinner("AI is finding solution of your code"):
                    Hints = Hints_Only(pil_image)
                    st.markdown(Hints)

            elif select == "Solution With Code":
                with st.spinner("AI is finding solution of your code"):
                    Fixed_result = Fixed_code(pil_image)
                    st.markdown(Fixed_result)








