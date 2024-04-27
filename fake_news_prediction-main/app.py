# import streamlit as st
# import pickle


# manual_testing = pickle.load(open('manual_testing.pkl', 'rb'))
# def main():
#     st.title("Fake News Prediction")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     content = st.text_input("content","Type Here")
#     result=""
#     if st.button("Predict"):
#         result=manual_testing(content)
#     st.success('The output is {}'.format(result))
#     if st.button("About"):
#         st.text("Lets LEarn")
#         st.text("Built with Streamlit")

# if __name__=='__main__':
#     main()

import streamlit as st
import pickle



def manual_testing(content):
    manual_testing = pickle.load(open('manual_testing.pkl', 'rb'))
    # Your prediction logic here
    return  
    

def main():
    st.title("Fake News Prediction")
    html_temp = """
    <div style="background-color: tomato; padding: 10px">
    <h2 style="color: white; text-align: center;">Fake News Prediction App</h2>
    </div>
    """
    

    st.markdown(html_temp, unsafe_allow_html=True)
    
    content = st.text_area("Enter the news content", "Type Here")
    
    result = ""
    if st.button("Predict"):
        if content:
            result = manual_testing(content)
        else:
            st.warning("Please enter some text.")
    
    st.success('The output is {}'.format(result))
    
    if st.button("About"):
        st.text("This is a simple fake news prediction app built with Streamlit.")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
