import streamlit as st

st.title('追思缅怀敬先烈，砥砺前行建新功')
if st.checkbox('为牺牲的先烈献花'):
    st.title('红色歌曲欣赏')
    if st.checkbox('欣赏"红色歌曲"'):
      with st.container():
        option = st.selectbox(
           '选择一首歌曲',
           ('黄河大合唱', '没有共产党就没有新中国','当那一天来临'))
        '👇以下歌曲是《',option,'》'
        if option=='黄河大合唱':
          audio_file = open('./黄河大合唱.wav', 'rb')
          audio_bytes = audio_file.read()
          st.audio(audio_bytes, format='audio/wav')
        elif  option=='没有共产党就没有新中国':
          audio_file = open('./没有共产党就没有新中国.wav', 'rb')
          audio_bytes = audio_file.read()
          st.audio(audio_bytes, format='audio/wav')
        elif  option=='当那一天来临':
          audio_file = open('./当那一天来临.wav', 'rb')
          audio_bytes = audio_file.read()
          st.audio(audio_bytes, format='audio/wav')

    st.title('欣赏红色视频')
    if st.checkbox('重温"红色歌经典"'):
      video_file = open('./长津湖.mp4', 'rb')
      video_bytes = video_file.read()

      st.video(video_bytes)
