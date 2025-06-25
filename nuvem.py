from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from transcricao import transcrever_audio

def gerar_nuvem(texto):
    stopwords = set(STOPWORDS)
    stopwords.update([
        'é', 'de', 'que', 'o', 'a', 'e', 'da', 'do', 'em', 'com', 'por', 'para', 'na', 'no', 'uma', 'como',
        'os', 'as', 'se', 'ao', 'à', 'não', 'mais', 'nos', 'já', 'também', 'são', 'isso', 'essa', 'esse',
        'então', 'tipo', 'né', 'tá', 'vai', 'vou', 'acho', 'pra', 'porque', 'gente', 'aí', 'foi', 'tem',
        'têm', 'todo', 'toda', 'todos', 'todas', 'falar', 'falando'
    ])
    nuvem = WordCloud(
        stopwords=stopwords,
        background_color="black",
        width=1600,
        height=800
    ).generate(texto)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(nuvem, interpolation='bilinear')
    ax.set_axis_off()
    return fig  # Retorne o fig para o Streamlit
