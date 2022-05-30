import scrapy

# TF-IDF
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from math import log10

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()


class QuotesSpider(scrapy.Spider):
    name = "tubes_novel2"

    def start_requests(self):
        main_Url = 'https://www.worldnovel.online/'
        Novel = 'imperial-god-emperor/'

         # list 10 url tiap chapter di novel imperial god emperor
        urls = [
            '{}{}chapter-1-four-year-champion/'.format(main_Url, Novel),
            '{}{}chapter-2-shock-heros-badge/'.format(main_Url, Novel),
            '{}{}chapter-3-does-my-decision-need-an-explanation/'.format(main_Url, Novel),
            '{}{}chapter-4-the-phoenix-and-the-loach/'.format(main_Url, Novel),
            '{}{}chapter-5-golden-meridians/'.format(main_Url, Novel),
            '{}{}chapter-6-the-shadow-of-the-divine-ancient-mountain/'.format(main_Url, Novel),
            '{}{}chapter-7-before-i-was-just-having-a-joke-with-you/'.format(main_Url, Novel),
            '{}{}chapter-8-no-compromise/'.format(main_Url, Novel),
            '{}{}chapter-9-bai-yuqing/'.format(main_Url, Novel),
            '{}{}chapter-10-its-not-that-he-cant-but-its-that-he-won/'.format(main_Url, Novel)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) # metode Scrapy meminta request ke web url

    def parse(self, response):
    #    print(response.url)
        # ekstrak data yang berasal dari selector css pada inspect element web untuk dijadikan sebuah text
        yield {
             'jdlChap' : response.css('#outer-wrapper > div > h3::text').extract(), # mengambil data Judul Chapter
             'textNovel' : response.css('#soop > p ::text').extract(),  # mengambil data berupaa seluruh isi teks novel yang terdapat dalam tag p
        }
    
    # block untuk proses TF-IDF function
    def get_list_of_word(list_of_chapNovel):
        list_of_word = []

        for sentence in list_of_chapNovel:
            for word in stemmer.stem(sentence).split(' '):
                if word not in list_of_chapNovel:
                    list_of_word.append(word)
        
        return list_of_word

    # membuka file yang berupa store data dari hasil ouput Scrapy tadi yang dimasukkan ke dalam sebuah file berformat json
    # yang mana untuk store data ke berupa file itu dilakukkan command Scrapy tertentu ke cmd, allu akan tebentuklah file tersebut

    # List yang berisi kumpulan teks chapter novel dan ukuran dari list tersebut
    list_of_chapNovel = [open('novel_imperial_god_emperor.json', encoding='utf-8').read()]
    length_of_chapNovel = len(list_of_chapNovel)


    # berisi kata-kata yang berasal dari list text chapNovel
    list_of_word = get_list_of_word(list_of_chapNovel)
    # print(list_of_word)
    print(list_of_word[17])
    print(list_of_word[44])
    print(list_of_word[99])
    print(list_of_word[120])
    print(list_of_word[155])
    print(list_of_word[267])
    print(list_of_word[289])
    print(list_of_word[375])
    print(list_of_word[402])
    print(list_of_word[689])





       
    