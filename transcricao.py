import whisper

def transcrever_audio(arquivo_audio="gravacao.wav"):    
 # (pode ser "tiny", "base", "small", etc.)
 modelo = whisper.load_model("small")
 
 resposta = modelo.transcribe("gravacao.wav", language="pt")
 resultado = resposta["text"]
#Precisa do return pois irei realizar manipulação com o output
 return resultado 

