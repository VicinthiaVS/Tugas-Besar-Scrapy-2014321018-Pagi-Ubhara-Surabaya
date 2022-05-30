import scrapy

# TF-IDF
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from math import log10

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()


class QuotesSpider(scrapy.Spider):
    name = "tubes_novel" # Spidername

    def start_requests(self):
        main_Url = 'https://www.worldnovel.online/'
        Novel = 'cultivation-chat-group/'

        # list 10 url tiap chapter di novel cultivation chat group 
        urls = [
            '{}{}chapter-1-mt-yellows-true-monarch-and-nine-provinces-1-group-indo/'.format(main_Url, Novel),
            '{}{}chapter-2-please-wait-for-esteemed-me-to-divinate-indo/'.format(main_Url, Novel), 
            '{}{}chapter-3-one-pill-recipe-indo/'.format(main_Url, Novel), 
            '{}{}chapter-4-h-citys-3rd-stage-houtian-lightning-tribulation-indo/'.format(main_Url, Novel),
            '{}{}chapter-5-i-believe-in-science-indo/'.format(main_Url, Novel),
            '{}{}chapter-6-copper-trigrams-immortal-master-indo/'.format(main_Url, Novel),
            '{}{}chapter-7-the-group-of-delinquents-that-got-wiped-out-indo/'.format(main_Url, Novel),
            '{}{}chapter-8-soft-feather-and-luo-xin-street-indo/'.format(main_Url, Novel),
            '{}{}chapter-9-the-other-luo-xin-street-indo/'.format(main_Url, Novel),
            '{}{}chapter-10-a-brief-interlude-while-strolling-in-the-streets-indo/'.format(main_Url, Novel)
            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) # metode Scrapy meminta request ke web url

    def parse(self, response):
    #    print(response.url)
        # ekstrak data yang berasal dari selector css pada inspect element web untuk dijadikan sebuah text
        yield {
             'jdlChap' : response.css('#outer-wrapper > div > h3::text').extract(), # mengambil data Judul Chapter
             'textNovel' : response.css('#soop > p ::text').extract(), # mengambil data berupaa seluruh Isi Teks novel yang terdapat dalam tag p
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
    # yang mana untuk store data ke berupa file itu dilakukkan command Scrapy tertentu ke cmd, lalu akan tebentuklah file tersebut

    # List yang berisi kumpulan teks chapter novel dan ukuran dari list tersebut
    list_of_chapNovel = [open('novel_cultivation_chat_group.json', encoding='utf-8').read()] # membaca file 
    length_of_chapNovel = len(list_of_chapNovel)


    # berisi kata-kata yang berasal dari list text chapNovel (TF-IDF)
    list_of_word = get_list_of_word(list_of_chapNovel)
    #print(list_of_word)
    print(list_of_word[1])
    print(list_of_word[25])
    print(list_of_word[36])
    print(list_of_word[49])
    print(list_of_word[62])
    print(list_of_word[100])
    print(list_of_word[233])
    print(list_of_word[278])
    print(list_of_word[345])
    print(list_of_word[400])





       
    