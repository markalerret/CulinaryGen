# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:29:52 2024

@author: mark
"""

from nltk.translate.bleu_score import corpus_bleu

references = [[['my', 'first', 'correct', 'sentence'], ['my', 'second', 'valid', 'sentence']]]
candidates = [['my', 'sentence']]
score = corpus_bleu(references, candidates)
print(candidates)
print(score)
print('\n')

candidates2 = [['my', 'first', 'correct', 'sentence']]
score2 = corpus_bleu(references, candidates2)
print(candidates2)
print(score2)
print('\n')

candidates3 = [['my', 'second', 'valid', 'sentence']]
score3 = corpus_bleu(references, candidates3)
print(candidates3)
print(score3)
print('\n')

candidates4 = [['my', 'correct', 'first']]
score4 = corpus_bleu(references, candidates4)
print(candidates4)
print(score4)
print('\n')

candidates5 = [['my', 'first', 'correct']]
score5 = corpus_bleu(references, candidates5)
print(candidates5)
print(score5)