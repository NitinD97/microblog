import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):

    list_of_translatable_languages = json.loads(
        requests.get('https://api.cognitive.microsofttranslator.com/languages?api-version=3.0').content)['translation'].keys() or \
                                     ['af', 'ar', 'bg', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es',
                                      'et', 'fa', 'fi', 'fil', 'fj', 'fr', 'he', 'hi', 'hr', 'ht', 'hu', 'id', 'is',
                                      'it', 'ja', 'ko', 'lt', 'lv', 'mg', 'mi', 'ms', 'mt', 'mww', 'nb', 'nl', 'otq',
                                      'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sm', 'sr-Cyrl', 'sr-Latn', 'sv', 'sw', 'ta',
                                      'te', 'th', 'tlh', 'to', 'tr', 'ty', 'uk', 'ur', 'vi', 'yua', 'yue', 'zh-Hans',
                                      'zh-Hant']
    if source_language not in list_of_translatable_languages or dest_language not in list_of_translatable_languages:
        return _('Error: Translator could not translate as this language is not in our translatable list!')
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY']}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
        return _('Error: Sorry could not translate!')
    return json.loads(r.content.decode('utf-8-sig'))
