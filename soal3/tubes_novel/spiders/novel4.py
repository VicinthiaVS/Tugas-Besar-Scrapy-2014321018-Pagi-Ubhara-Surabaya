import scrapy

# TF-IDF
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from math import log10

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()


class QuotesSpider(scrapy.Spider):
    name = "tubes_novel4"

    def start_requests(self):
        main_Url = 'https://www.worldnovel.online/'
        Novel = 'embers-ad-infinitum/chapter-'

        # list 10 url tiap chapter di novel embers ad infinitium 
        urls = [
            '{}{}1-/'.format(main_Url, Novel),
            '{}{}2-/'.format(main_Url, Novel),
            '{}{}3-/'.format(main_Url, Novel),
            '{}{}4-/'.format(main_Url, Novel),
            '{}{}5-/'.format(main_Url, Novel),
            '{}{}6-/'.format(main_Url, Novel),
            '{}{}7-/'.format(main_Url, Novel),
            '{}{}8-/'.format(main_Url, Novel),
            '{}{}9-/'.format(main_Url, Novel),
            '{}{}10-/'.format(main_Url, Novel)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # metode Scrapy meminta request ke web url

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
    # yang mana untuk store data ke berupa file itu dilakukkan command Scrapy tertentu ke cmd, allu akan tebentuklah file tersebut

    # List yang berisi kumpulan teks chapter novel dan ukuran dari list tersebut
    list_of_chapNovel = [open('novel_embers_infinitium_chapter.json', encoding='utf-8').read()]
    length_of_chapNovel = len(list_of_chapNovel)


    # berisi kata-kata yang berasal dari list text chapNovel
    list_of_word = get_list_of_word(list_of_chapNovel)
    # print(list_of_word)
    print(list_of_word[45])
    print(list_of_word[656])
    print(list_of_word[696])
    print(list_of_word[730])
    print(list_of_word[789])
    print(list_of_word[920])
    print(list_of_word[990])
    print(list_of_word[1000])
    print(list_of_word[1001])
    print(list_of_word[1100])





       
    