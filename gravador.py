import pyaudio
import wave
import os

def gravar_audio(tempo=20, arquivo_saida="gravacao.wav"):
    """
    Grava áudio do microfone por 'tempo' segundos e salva em 'arquivo_saida'.
    Retorna o caminho do arquivo salvo ou uma mensagem de erro.
    """
    try:
        audio = pyaudio.PyAudio() # cria o objeto
        stream = audio.open(
            input=True,
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            frames_per_buffer=1024
        ) #abre a captura de audio e configura 
        frames = [] # essa lista vai receber os bloco de audio

        for _ in range(0, int(44100 / 1024 * tempo)):
            bloco = stream.read(1024)
            frames.append(bloco)

        stream.stop_stream() # para de gravar
        stream.close() # fecha o audio
        audio.terminate() # libera os recurso do pyaudio

        with wave.open(arquivo_saida, "wb") as arquivo_final:
            arquivo_final.setnchannels(1)
            arquivo_final.setframerate(44100)
            arquivo_final.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            arquivo_final.writeframes(b"".join(frames))

        return arquivo_saida  # Retorna o caminho do arquivo para o Streamlit usar

    except Exception as e:
        return f"Erro ao gravar áudio: {e}"
