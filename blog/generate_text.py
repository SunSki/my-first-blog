from django.conf import settings
import markovify

def generate_text(sentence_num):
    path = '/blog/static/text/splitted_text.txt'
    splitted_text = ''
    sentence_list = []

    with open( settings.BASE_DIR + path, 'r' ) as f:
        splitted_text = f.read()

    text_model = markovify.NewlineText( splitted_text, state_size=3 )

    for _ in range(sentence_num):
        while True:
            sentence = text_model.make_sentence(tries=10)
            if sentence is not None:
                break
        sentence_list.append( ''.join(sentence.split()) )

    return sentence_list