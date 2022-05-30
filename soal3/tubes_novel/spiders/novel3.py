import scrapy

# TF-IDF
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from math import log10

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()


class QuotesSpider(scrapy.Spider):
    name = "tubes_novel3"

    def start_requests(self):
        main_Url = 'https://www.worldnovel.online/'
        Novel = 'historys-strongest-senior-brother/hssb-'

        # list 10 url tiap chapter historys strongest senior brother
        urls = [
            '{}{}chapter-1-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-2-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-3-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-4-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-5-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-6-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-7-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-8-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-9-indonesian/'.format(main_Url, Novel),
            '{}{}chapter-10-indonesian/'.format(main_Url, Novel)
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
    # yang mana untuk store data ke berupa file itu dilakukkan command Scrapy tertentu ke cmd, allu akan tebentuklah file tersebut

    # List yang berisi kumpulan teks chapter novel dan ukuran dari list tersebut
    list_of_chapNovel = [open('novel_historys_strongets_senior_b.json', encoding='utf-8').read()]
    length_of_chapNovel = len(list_of_chapNovel)


    # berisi kata-kata yang berasal dari list text chapNovel
    list_of_word = get_list_of_word(list_of_chapNovel)
    # print(list_of_word)
    print(list_of_word[55])
    print(list_of_word[432])
    print(list_of_word[569])
    print(list_of_word[600])
    print(list_of_word[700])
    print(list_of_word[777])
    print(list_of_word[811])
    print(list_of_word[880])
    print(list_of_word[921])
    print(list_of_word[980])





       
    