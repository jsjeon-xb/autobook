import streamlit as st

def main(param1, param2, param3, param4, param5):
    st.title("My Streamlit App")
    st.write("Parameter 1:", param1)
    st.write("Parameter 2:", param2)
    st.write("Parameter 3:", param3)
    st.write("Parameter 4:", param4)
    st.write("Parameter 5:", param5)

if __name__ == '__main__':
    param1 = st.text_input("Enter parameter 1:")
    param2 = st.slider("Select parameter 2:", 0, 100, 50)
    param3 = st.selectbox("Select parameter 3:", ["Option 1", "Option 2", "Option 3"])
    param4 = st.checkbox("Select parameter 4")
    param5 = st.text_area("Enter parameter 5:")
    main(param1, param2, param3, param4, param5)