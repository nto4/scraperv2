import requests
import re
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer
import multiprocessing
import check_mail

res_per_page = []


def write_results(match):
    global res_per_page
    res_per_page.append(match)



def write_results_final(tmp):
    tmp = set(tmp)
    tmp = list(tmp)
    name = multiprocessing.current_process().name
    with open("results/"+str(name) + "result.txt", "a+") as file_object:
        for m in tmp:
            file_object.write("\n" + str(m))



def extract_mails(page_content):
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', page_content)
    return match


def myMain(URL):
    pages = get_main_page(URL)
    tmp = []
    for page in pages:
        if len(page) > 0:
            if page[0] == '/':
                tmp.append(URL + page)
            elif page == URL + '/':
                pass
            elif page[0] == 'h':
                tmp.append(URL)
            elif page[0] == "#":
                pass
            else:
                pass

    tmp = set(tmp)
    tmp = list(tmp)

    for i in tmp:
        get_mail_from_page(i)


def get_main_page(URL):
    pages = []
    headersparam = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    page_content = requests.get(URL, headers=headersparam).content
    for link in bs(page_content, "html.parser", parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            pages.append(link['href'])

    pages.append(URL)
    return pages

    # return pages


def get_mail_from_page(URL):
    headersparam = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    try:
        # print(URL)
        page_content = str(requests.get(URL, headers=headersparam).content)
        extractet_mails = extract_mails(page_content)
        extractet_mails = check_mail.check_mails(extractet_mails)
        extractet_mails = set(extractet_mails)
        extractet_mails = list(extractet_mails)
        if len(extractet_mails) > 0:
            for i in extractet_mails:
                if i in res_per_page:
                    pass
                else:
                    write_results(i)
    except:
        pass


def runIt(URL):
    try:
        name = multiprocessing.current_process().name
        myMain(URL)
        write_results_final(res_per_page)
        with open("succes/" + str(name) + "succes.log", "a+") as file_object:
            file_object.write(str(URL) + "\n")
    except Exception as e:
        name = multiprocessing.current_process().name
        with open("error/" + str(name) + "error.log", "a+") as file_object:
            file_object.write(str(URL) + " : " + str(e) + "\n")
