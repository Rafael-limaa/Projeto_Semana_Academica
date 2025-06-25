import streamlit as st
from gravador import gravar_audio
from transcricao import transcrever_audio
from nuvem import gerar_nuvem
import os

st.title("Gravador de Áudio + Transcrição + Nuvem de Palavras")

# Slider para tempo de gravação
tempo = st.slider("Tempo de gravação (segundos)", min_value=5, max_value=60, value=20)

if st.button("Gravar áudio"):
    with st.spinner("Gravando..."):
        caminho = gravar_audio(tempo=tempo)
    if os.path.exists(caminho):
        st.success(f"Áudio gravado em: {caminho}")
        audio_file = open(caminho, 'rb')
        st.audio(audio_file.read(), format='audio/wav')

        # Transcrição automática
        with st.spinner("Transcrevendo..."):
            texto = transcrever_audio(caminho)
        st.success("Transcrição concluída!")
        st.text_area("Texto transcrito:", texto, height=300)

        # Nuvem de palavras automática
        with st.spinner("Gerando nuvem de palavras..."):
            fig = gerar_nuvem(texto)
        st.pyplot(fig)
        st.success("Nuvem de palavras gerada com sucesso!")
    else:
        st.error(caminho)