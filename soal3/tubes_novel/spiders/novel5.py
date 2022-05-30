import scrapy

# TF-IDF
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from math import log10

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()


class QuotesSpider(scrapy.Spider):
    name = "tubes_novel5"

    def start_requests(self):
        main_Url = 'https://www.worldnovel.online/'
        Novel = 'the-first-order/'

        # list 10 url tiap chapter di novel the first order
        urls = [
            '{}{}chapter-1-a-sickness-in-the-head/'.format(main_Url, Novel),
            '{}{}chapter-2-this-world-has-never-trusted-tears/'.format(main_Url, Novel),
            '{}{}chapter-3-a-palace/'.format(main_Url, Novel),
            '{}{}chapter-4-luck-is-a-type-of-skill-too/'.format(main_Url, Novel),
            '{}{}chapter-5-the-school/'.format(main_Url, Novel),
            '{}{}chapter-6-walls-and-science/'.format(main_Url, Novel),
            '{}{}chapter-7-substitute-teacher/'.format(main_Url, Novel),
            '{}{}chapter-8-something-really-is-wrong-with-his-head/'.format(main_Url, Novel),
            '{}{}chapter-9-ask-me-if-theres-anything-you-dont-understand/'.format(main_Url, Novel),
            '{}{}chapter-10-side-quest/'.format(main_Url, Novel)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) # metode Scrapy meminta request ke web url

    def parse(self, response):
    #    print(response.url)
        yield {
             'jdlChap' : response.css('#outer-wrapper > div > h3::text').extract(), # mengambil data Judul Chapter
             'textNovel' : response.css('#soop > p ::text').extract(), # mengambil data berupaa seluruh isi teks novel yang terdapat dalam tag p
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
    list_of_chapNovel = [open('novel_the_first_order.json', encoding='utf-8').read()]
    length_of_chapNovel = len(list_of_chapNovel)


    # berisi kata-kata yang berasal dari list text chapNovel
    list_of_word = get_list_of_word(list_of_chapNovel)
    # print(list_of_word)
    print(list_of_word[25])
    print(list_of_word[688])
    print(list_of_word[702])
    print(list_of_word[899])
    print(list_of_word[917])
    print(list_of_word[918])
    print(list_of_word[1200])
    print(list_of_word[1400])
    print(list_of_word[1539])
    print(list_of_word[1993])





       
    