import urllib.request
from bs4 import BeautifulSoup

class DataReader:
    def __init__(self, url):
        self.url = url

    def read_data(self):
        source = urllib.request.urlopen(self.url)
        raw_text = source.read()
        output = raw_text.decode('utf-8')
        source.close()
        return output

class DataParser:
    def __init__(self, page_source):
        self.page_source = page_source

    def parse_data(self):
        soup = BeautifulSoup(self.page_source, 'lxml')
        teachers_list = []
        for con in soup.find_all('div', {'class': 'names-list'}):
            for teachers in con.find_all('li'):
                teachers_list.append(teachers)
        new_str = []
        for field in teachers_list:
            field = str(field)
            tmp = field[field.find('<li>') + 4: field.find('</li>')]
            if not tmp.find('</a>') == -1:
                tmp = tmp[tmp.find('>', 4) + 1: tmp.find('</a>')]
            if not tmp.find('<strong>') == -1:
                tmp = tmp[tmp.find('<strong>') + 8 : tmp.find('</strong>')]
            tmp = tmp.strip()
            new_str.append(tmp)
        return new_str

obj = DataReader('http://www.jedynka.zgora.pl/?show=kadra')

site_content = DataParser(obj.read_data())
cn = site_content.parse_data()

for i in cn:
    print(i)