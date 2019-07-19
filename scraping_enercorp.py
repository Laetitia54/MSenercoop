import numpy as np
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json

dico_Ques_Resp = {}

# fonction pour générerun temps aléatoire entre les click
def generate_number_delay():
    """
    Retourne un chiffre aléatoire suivant une distribution normal de moyenne 4 secondes et d'ecart-type de 0.8
    Ce chiffre aléatoire est le délai après chaque clic. Le but est de simuler le comportement d'un humain :
    un délai fixe peut attirer l'attention des contrôleurs, tout comme un délai aléatoire d'une distribution uniforme
    """
    mean = 2
    sigma = 0.8
    delai = np.random.normal(mean,sigma,1)[0]
    while delai<0:
        delai = np.random.normal(mean,sigma,1)[0]
    time.sleep(delai)


#choix du navigateur 
browser = webdriver.Chrome()

# choix du site 
browser.get('https://www.enercoop.fr/')

#Clic vers le lien FAQ
faq = browser.find_element_by_xpath('//*[@id="block-nrc-main-nrc-main-sticky"]/div/div/div/div/div/div[1]/a')
faq.click()
generate_number_delay()

# 'Je ne suis pas encore client' et 'Je suis déjà client'
question_reponse = browser.find_elements_by_css_selector('li.blocks-item')
question_reponse[0].click()
generate_number_delay()

# section des 
sections = browser.find_elements_by_css_selector("h3.section-tree-title a")

for section in range(len(sections)) :
    sections = browser.find_elements_by_css_selector("h3.section-tree-title a")
    sections[section].click()
    generate_number_delay()
    click_articles = browser.find_elements_by_css_selector('li.article-list-item a')
    for click_article in range(len(click_articles)) :
        click_articles = browser.find_elements_by_css_selector('li.article-list-item a')
        click_articles[click_article].click()
        
        question = browser.find_element_by_tag_name('h1')
        response = browser.find_element_by_class_name('article-body')
        dico_Ques_Resp[question.text] = response.text        
        generate_number_delay()
        browser.back()

    generate_number_delay()
    browser.back()

generate_number_delay()
browser.back()

question_reponse = browser.find_elements_by_css_selector('li.blocks-item')
question_reponse[1].click()

# section des 
sections = browser.find_elements_by_css_selector("h3.section-tree-title a")

for section in range(len(sections)) :
    sections = browser.find_elements_by_css_selector("h3.section-tree-title a")
    sections[section].click()
    generate_number_delay()
    click_articles = browser.find_elements_by_css_selector('li.article-list-item a')
    for click_article in range(len(click_articles)) :
        click_articles = browser.find_elements_by_css_selector('li.article-list-item a')
        click_articles[click_article].click()
        
        question = browser.find_element_by_tag_name('h1')
        response = browser.find_element_by_class_name('article-body')
        dico_Ques_Resp[question.text] = response.text        
        generate_number_delay()
        browser.back()

    generate_number_delay()
    browser.back()

generate_number_delay()
browser.back()


with open('result.json', 'w') as fp:
    json.dump(dico_Ques_Resp, fp)

fin = pd.DataFrame({'question' : [], 'response' : [] })
for key, value in dico_Ques_Resp.items() :
    fin = fin.append({'question' : key, 'response' : value }, ignore_index=True)

fin.to_csv('enercorp.csv')