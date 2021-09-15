import streamlit as st
import preprocessor,helpers
st.sidebar.title('Hello, guru')
uploaded_file=st.sidebar.file_uploader('Choose a file')
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=preprocessor.preprocess(data)
    st.dataframe(df)
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')
    selected_user=st.sidebar.selectbox('Show Analysis',user_list)
    if st.sidebar.button('Show Analysis'):
        num_messages,words,num_media_messages,links=helpers.fetch_stats(selected_user,df)
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.header('Total messages')
            st.title(num_messages)
        with col2:
            st.header('Total words')
            st.title(words)
        with col3:
            st.header('Total media messages')
            st.title(num_media_messages)
        with col4:
            st.header('Total links')
            st.title(links)
