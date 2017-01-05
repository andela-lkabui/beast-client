import os
import json

import requests

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

BASE_URL = 'https://od-api.oxforddictionaries.com/api/v1'


def credentials():
    """
        Obtains the Oxford API app id and secret key from their respective
        environment variables.
    """
    return {
        'app_id': os.environ['APP_ID'],
        'app_key': os.environ['APP_KEY']
    }


def search(request):
    """
        Renders the search page if query parameter 'word_id' does not exist.

        If the query parameter 'word_id' exists, this method retrieves its
        value and queries the oxford dictionary api for its definition, example
        usage and available synonyms.
    """
    if 'word_id' in request.GET:
        full_url = '{0}/entries/en/{1}'.format(
            BASE_URL, request.GET['word_id'])

        headers = credentials()
        resp = requests.get(full_url, headers=headers)
        # If no such word exists
        if resp.status_code == 404:
            context = {
                'word_id': request.GET['word_id']
            }
            return render(request, 'not_found.html', context)

        lex_entries = resp.json()['results'][0]['lexicalEntries'][0]

        context = {
            'word_id': request.GET['word_id'],
            'phonetic': lex_entries['pronunciations'][0]['phoneticSpelling'],
            'lex_cat': lex_entries['lexicalCategory'],
            'definition': lex_entries['entries'][0]['senses'][0]['definitions'][0],
        }
        # some words don't have example usage, hence the "or" part
        examples = lex_entries['entries'][0]['senses'][0].get('examples') or []
        context['examples'] = []
        for example in examples:
            context['examples'].append(example['text'])

        # some words don't have pronounciation audio, hence the "or" part
        context['audio'] = lex_entries['pronunciations'][0].get('audioFile')\
            or ''

        full_url = '{0}/synonyms'.format(full_url)
        resp = requests.get(full_url, headers=headers)

        # if the word has no synonyms
        if resp.status_code == 404:
            context['synonyms'] = 'N/A'
        else:
            root = resp.json()['results'][0]['lexicalEntries'][0]['entries'][0]
            synonym_list = root['senses'][0]['synonyms']
            
            synonyms = []
            for synonym in synonym_list:
                synonyms.append(synonym['text'])
            context['synonyms'] = ', '.join(synonyms)

        return render(request, 'found.html', context)
        
    return render(request, 'search.html')