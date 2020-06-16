from tkinter import *
import os
import tkinter.ttk as ttk
import random
import time

tombala=["el","le","ele","elle",
         "al","la","ala","alla","Ela","ela","Lale","lale",
         "ek","ke","ak","ka","kek","kal","kalk","kel","kale","elek","keke","kelle","kelek","elekle","ekle","leke","kekle","akla",
         "il","li","ik","ki","elli","iki","ile","ilke","İlke","Ali","eki","keki","eli","laleli","ekli","kil","killi","lila","ilk","ilik","ilikle",
         "keklik","lekeli","kekik","ikili","elekli","kekikli","ikilik","ilkel","ilkeli","Akile",
         "en","ne","an","na","in","ni","ana","Nil","anne","nane","ninni","İnan","Nalan","elin","kan","eken","kanal","kalan","kene","Alkan",
         "anla","inle","nine","inek","nal","Kenan","İnal","ilan","ekin","neli","alan","inan","lakin","kanka","enli","kalkan","enik","nakil",
         "ol","lo","ok","ko","on","no","ona","eko","kok","kol","kon","kola","kilo","konak","koli","kokla","alo","Okan","kano","ikon","nano",
         "ekol","koni","okka","olanak",
         "em","me","ma","im","mi","om","mo","mola","mani","mal","kalem","ekmek","kelime","Melek","Melike","limon","alma","Melik","kilim","mala",
         "Emin","Emine","liman","mama","keman","kalemlik","komi","minik","lokma","iklim","Kamil","Kamile","almak","elma","kemik","ama","nem","nemli",
         "Mine","mekik","Emel","kimlik","Leman","Kemal","Alim","komik","mini","maki","makine","mil","emekli","milli",
         "ul","lu","uk","ku","un","nu","um","mu","kule","onlu","kumlu","lokum","un","unlu","kul","kilolu","ulu","kolu","kollu","konu","konuk","onluk",
         "kum","mum","kukla","oku","okul","koku","Memmune","kokulu","konum","kolum","mumluk","Numan","limonlu","limonluk","kulak","okuma","kanun","ilkokul",
         "memnun","et","te","at","ta","it","ti","ot","to","ut","tu","tak","tek","tane","ton","tok","tel","taka","atla","atlet","teke","kot","Ata","Tan","Altan",
         "tekne","tulum","tonton","tut","mont","toka","kat","kutu","tat","ten","atma","tatma","Onat","etli","taneli","kent","kilit","koltuk","alt","kanat","net",
         "itme","Umut","tilki","teneke","anlat","laka","tam","not","Atakan","olta","Talat","kutla","teke","tele","omlet","Utku","Mete","Tekin","tatil","nokta",
         "etek","ül","lü","ük","kü","ün","nü","üm","mü","üt","tü","ünlü","ülke","Ümit","ütü","küme","kül","küllük","Ülkü","tünel","tül","tüm","lüle","ünlem",
         "ünite","menü","Tülin","Ünal","küt","kütük","tüt","mülk","akü","kütle","mümkün",
         "ey","ye","ay","ya","iy","yi","oy","yo","uy","yu","üy","yü","uyan","yak","yut","kay","koy","Kaya","ayak","yatak","yaya","koyu","alay","maya","Yaman",
         "yayla","naylon","Yemen","leylak","oyun","yalan","maymun","yutmak","kamyon","oyna","Kutay","yumak","yitik","yelken","Aylin","eylül","Ayla","Oktay",
         "uyku","oyna","yanak","tüy","Leyla","koyun","kaykay","kolay","yay","Konya","Antalya","Antakya","Eymen","leylek","yeni","yemin","üye","iyi","kamyonet",
         "kimyon","yün","yük","kalay","tay","Ayten","yelek","yakma","yol","Aykut","yemek","kolye","kaymak","kuyu","kayak","Oya","Tülay",
         "öl","lö","ök","kö","ön","nö","öm","mö","öt","tö","öy","yö","yön","köy","köylü","öykü","önlük","önem","önemli","kök","Önal","öteki","kötü","önlem",
         "öyle","kötülük","yöntem","atölye","yönet","yönetmen","ölü","ötme","ölme","köle","Öktem",
         "er","re","ar","ra","ir","ri","or","ro","ur","ru","ür","rü","ör","rö","nar","Rana","türlü","kemer","rüya","Meryem","armut","tekerleme","tekerlek",
         "türkü","turna","ara","iri","örtü","kare","tür","ürkek","Türkiye","yumurta","market","mimar","ikram","Onur","mantar","atari","Ömer","erik","internet",
         "korna","tamir","Turan","traktör","erken","kömür","torun","raket","orman","ortak","kertenkele","marul","terlik","mart","İlter","örnek","roket","yer",
         "mermer","Eren","İrem","ayran","orta","Mert","tarla","kar","makarna","kor","kör","kumru","ray","tur","Ertan","yar","kir","kur","koro","mor","Nur","Nuri",
         "yor","erkek","Eray","iri","karton","kural","kuru","Murat","Ömür","tanker","tarak","arka","Emre","karne","kira","korku","kurak","lira","tere","terli",
         "tören","yürek","Atatürk","ileri","litre","yirmi","makara","kara","yara","tur","arka","mera","kura","küre","rota","ürün","Türk","renk","tart","tren",
         "aktan","marka","metre","metro","roman","irmik","kartal","kamera","numara","maraton","karakol","Nuran","Tarkan","Kerem","Erkan","rol","kart","yurt",
         "Aynur","Taner","Koray","Ankara","roka","kürek","Erol",
         "ıl","lı","ık","kı","ın","nı","ım","mı","ıt","tı","ıy","yı","ır","rı","kır","kırk","altı","ırmak","tatlı","yık","yıka","atkı","tanı","tırnak","kırık",
         "tırtıl","kıyma","yırtık","yarım","martı","arı","ayı","altın","ılık","katır","takı","tırmık","yukarı","tırman","yılan","tartı","tanıt","kına","Itır",
         "mantı","Anıl","Tarık","ayır","aylık","kıl","kıt","kıy","yıl","akıl","alın","anıt","atık","kayık","kıta","yakın","Akın","kalın","katı","yalın","aralık",
         "yaralı","yatılı","kıyı","takım","yanıt","ayrı","Namık","karın","kulaklık","yıllık","anı","atlı","aynı","artı","yakıt","tanık","Alkın","tır",
         "ed","de","ad","da","id","di","od","do","ud","du","üd","dü","öd","dö","ıd","dı","dik","dut","dur","dede","Demet","dünya","diken","Dilek","kedi","düdük",
         "dantel","dümen","dinle","dol","dayı","dam","döner","Didem","yedi","doktor","dana","doy","Damla","Döndü","dürüm","dört","dolu","duman","direk","dar","dem",
         "dil","duy","dök","dal","der","din","ada","Eda","damak","demir","delik","demlik","dolma","durak","Kadir","maden","moda","nadir","Arda","damar","dikkat",
         "dudak","mide","müdür","ördek","dondurma","kardelen","kurdele","orkide","koridor","Ender","Dilara","dert","denk","dilim","Erdem","Derya","ad","adam","dama",
         "radyo","damat","dedi","nerede","mendil","kaldırım","dün","ödül","Aydın","Duru","Adem","Erdal","Önder","darı",
         "es","se","as","sa","is","si","os","so","us","su","üs","sü","ös","sö","ıs","sı","sarı","salı","sayı","Seda","Selin","Sema","tenis","Selim","say","sulu","simit",
         "sus","soru","taksi","Suna","süs","Sinan","Selma","sanmak","süslü","salatalık","mısır","sarımsak","süt","kestane","kayısı","susam","tost","uslu","askı","ıslak",
         "üst","Sadık","eski","soda","sıkı","Seren","seksek","sert","Esin","sinema","sandalye","usta","sütlü","saksı","istasyon","Samsun","Ersin","ses","sil","san","sat",
         "sel","sor","asker","masa","Osman","sakal","Mars","sandal","Melisa","sıra","istek","maske","sokak","Sıtkı","sanat","serin","sinek","süre","lastik","seramik",
         "Soner","domates","saniye","Selami","dans","lüks","Sinem","ders","sark","Kars","kurs","sırt","Aslı","Esra","Semra","Sıla","asansör","sokak","İlyas","asla",
         "yastık","elmas","kasa","saklan","nisan","sök","insan","doksan","sandık","adres","ısrar","Kasım","sön","dost","öksürük","dirsek","sönük","salon","sökük","sakin",
         "sarma","Asya","aslan","ast","Esma","esmer","Asu","esne","esnek","ıslık","iste","İsmet","saman","Selinay","son","Sümer","kas","Sami","testere","Dursun","Melis",
         "Mersin","sık","sen","Sude","sosis","sır","Yasin","kes",
         "eb","be","ab","ba","ib","bi","ob","bo","ub","bu","üb","bü","öb","bö","ıb","bı","baba","balık","balon","bardak","bal","balkon","bebek","Banu","abla","bayrak",
         "börek","Betül","Burak","boya","ayakkabı","Birol","sabun","Bekir","Ebru","bilet","Berat","Bayram","bir","birlik","akraba","akbaba","kelebek","büyük","oba","balina",
         "leblebi","balta","bant","ban","bana","besle","büyüt","ebe","ben","bekle","birlikte","biber","bas","bel","bil","boy","bay","bayan","bık","bin","bot","böl","bakla",
         "bamya","banyo","beton","berber","bıyık","bidon","bilim","boru","sabır","Sabri","bütün","badem","bakkal","banka","baston","beyin","bırak","bulut","kabak","barbunya",
         "bataklık","basketbol","beslenme","battaniye","belediye","burs","kalabalık","Berk","boks","bor","büst","Berkay","Basri","Baran","Belma","Berna","Birkan","Bora","bülbül",
         "bak","bisiklet","araba","bale","balo","bone","bina","bere","büro","obur","kibar","subay","nöbet","Buket","tabak","bordo","biblo","tablo","tebrik","sümbül","dürbün",
         "tombul","kibrit","tablet","sembol","abaküs","otobüs","elbise","biberon","kulübe","mobilya","İstanbul","Bilal","Kübra","Sibel","Buse","beste","tabure","Belkıs","Berke",
         "basit","bayat","besin","bilye","burun","böbrek","bey","lamba","Bartın","torba","beraber","Batman","but","robot","Kubat","Tibet","Berkant","Baki","batı","bakır","balerin",
         "balet","baskül","Beril","soba",
         "ez","ze","az","za","iz","zi","oz","zo","uz","zu","üz","zü","öz","zö","ız","zı","yaz","kız","yüz","taze","teyze","zaman","kaza","zil","zor","Öznur","imza","kırmızı","ziyaret",
         "bilezik","kazak","zeytin","yazı","yüzük","zar","kez","bozuk","üzüm","kuzu","zebra","süz","koza","köz","izin","Zeki","emzik","kiraz","Yıldız","İzmir","tez","kazı","titiz","zemin",
         "zarar","saz","sazlık","söz","tuz","dokuz","ikiz","düz","muz","biraz","Kezban","Nazlı","Özen","uzan","uzak","yaramaz","müzik","yazar","boz","diz","kaz","biz","buz","naz","siz","ayaz",
         "sazan","zam","imza","kızak","kuzey","Ozan","Özlem","sebze","uzak","zıt","sez","uzman","zambak","beyaz","bornoz","Deniz","dizi","omuz","Rıza","sekiz","öküz","sözlük","uzay","Zerrin","zımba",
         "düzenli","Kızılay","Zekiye","dize","mızıka","Ramazan","sızla","sızı","terazi","uzamak","Denizli","İzzet","düzine","Remzi","Remziye","temiz","temizlik","üzüntü","zararlı","tazı","buzdolabı",
         "Kazım","Suzan","nezle","Beyza","özür","kızamık","Arzu","İzel","Özkan","Zübeyde","Sezen","Azra","toz","bez","kazma","müze","boza","baza","otuz","Niyazi","Nazmi","uzun","ıssız","kazan","leziz",
         "rozet","sakız","tuzak","zurna","Özer","Nazmiye","terzi","yazlık","telsiz","balyoz","benzin","boynuz","mızrak","mazot","bbezelye","zat","kurnaz","dinazor","zerdali","bazlama","manzara","Ziya",
         "Sezer","Nazan","Aziz","Zeynel","Zümrüt","zabıta",
         "eç","çe","aç","ça","iç","çi","oç","ço","uç","çu","üç","çü","öç","çö","ıç","çı","çek","çiçek","reçel","çörek","çemen","çukur","çatal","çınar","çaydanlık","çikolata","taç","amaç","kaç","saç",
         "seç","çiz","çim","çit","sarkaç","çil","çak","çay","çal","çam","çekiç","sanatçı","çekirdek","reçete","maç","çadır","Çorum","keçi","çık","çayır","çatı","çoban","araç","serçe","Çetin","çabuk",
         "çanta","alçak","çıkarma","çok","çorba","çakıl","burç","seçim","dinç","Erdinç","çardak","çöl","çene","çök","koç","çözüm","alçı","ilçe","çıban","salça","sütçü","uçak","çare","çerez","çizme",
         "çürük","ilaç","kaçak","ölçü","Türkçe","bekçi","dilekçe","kemençe","balıkçı","büyüteç","çimento","çelik","nöbetçi","simitçi","çorak","biç","uçurtma","çark","borç","Seçil","Meriç","çakmak",
         "çömlek","Ayça","çimen","Çankırı","çan","suç","çaba","çeyiz","bıçak","çakı","çamur","çubuk","çanak","sıçra","çünkü","sütlaç","tarçın","çelenk","çeyrek","Çisem","çirkin","inatçı","suçsuz",
         "suçlu","çökelek","çember","çiçeklik","Tunç","Seçkin","yamaç","Sertaç","Açelya","Çin","çalı","küçük","açık","açlık","saçma","kılıç","buçuk","çamlık","Selçuk","Yalçın","Miraç","çita","çıta",
         "keçe","okçu","üçüz","çakal","çalım","Çilem",
         "eg","ge","ag","ga","ig","gi","og","go","ug","gu","üg","gü","ög","gö","ıg","gı","gel","ger","gez","geç","gam","gar","gaz","git","giy","gir","güz","gün","gür","güç","gör","göz","göl","gol",
         "gök","güç","göm","örgü","gemi","gezi","gazi","gaga","gıda","geyik","gazoz","goril","gelin","gitar","göbek","giyim","güzel","üçgen","kargo","dergi","giysi","silgi","karga","sargı","saygı",
         "bilgi","çalgı","gizli","üzgün","gömlek","güllaç","günlük","sünger","yangın","yengeç","yüzgeç","zengin","yorgan","düzgün","dalgıç","bulgur","mangal","garson","gazete","ızgara","sigorta","çekirge",
         "gezegen","Ege","çıngırak","bilgisayar","gökyüzü","günaydın","gürültü","gelin","gözlük","Giray","süzgeç","ilgi","çizgi","Gülendam","gezgin","güney","uygun","kasırga","dalgalı","gözleme","gösteri",
         "genel","belge","denge","sergi","gölet","gül","gergedan","Ezgi","Özge","gaye","Müge","engin","gönül","Güler","Gizem","Gülay","Bilge","Duygu","Tolga","Gamze","Gürkan","Belgin","Turgay","Gökçe",
         "Sezgin","Gözde","Bengü","Gökay","Göksel","Günay","Gülçin","Gülten","Gülsüm","Gülnur","Nurgül","Görkem","Özgür","Nergiz",
         "eş","şe","aş","şa","iş","şi","oş","şo","uş","şu","üş","şü","öş","şö","ış","şı","şen","şey","şal","şan","şiş","şok","şık","loş","yaş","kaş","kış","koş","kuş","taş","tuş","baş","beş","boş","dış","diş",
         "duş","düş","aşı","şaka","meşe","köşe","şişe","ateş","ataş","eşek","yaşa","işte","kişi","ışık","şort","akşam","alkış","galoş","geniş","yeşil","şekil","kaşık","karış","taşıt","şubat","şölen","döşek","şeker",
         "beşik","güreş","kumaş","turşu","çeşme","çarşı","komşu","şarkı","koşma","başka","başkan","boşluk","kardeş","şişman","baykuş","kaşkol","şimşek","şalgam","şamdan","aşure","enişte","şömine","neşeli",
         "Şakir","tebeşir","arkadaş","bulaşık","çamaşır","menekşe","şırınga","gözyaşı","şemsiye","üşümek","düşünmek","Şule","Neşe","Barış","Şamil","Başak","Şermin","Ayşe","Yaşar","Yeşim","Şenay","Gülşen",
         "koşu","Şaban","Şener","Şeyma","Şükrü","Büşra","Şükran","Şebnem","Şengül","Şadiye","güneş","şirin","şerbet","şaşkın","Rüştü","şenlik","şut","adaş","alkış","şerit","eşit","karış","yarış","Ayşegül",
         "şelale","müşteri","yumuşak","köşk","marş","şans","teşekkür","şaşı","maşa","yaşlı","dolmuş","gümüş","sarmaşık",
         "ec","ce","ac","ca","ic","ci","oc","co","uc","cu","üc","cü","öc","cö","ıc","cı","can","cam","acı","ince","inci","cici","cila","önce","amca","cami","cuma","baca","acil","ocak","ceza","gece","izci","kanca",
         "cüce","incir","ücret","ceket","böcek","sıcak","sucuk","çocuk","mucit","cacık","bacak","balcı","yonca","cimri","cirit","coşku","cesur","camcı","gonca","yolcu","cümle","zincir","meclis","sözcük",
         "boncuk","bencil","ceylan","tüccar","acemi","acele","cüzdan","ikinci","açacak","eczacı","eczane","kiracı","satıcı","koşucu","oyuncu","şakacı","eskici","atmaca","boyacı","kaleci","yiyecek","oduncu",
         "birinci","karınca","oyuncak","dilenci","düşünce","dönerci","kızılcık","çorbacı","turşucu","taksici","bulmaca","bilmece","çekmece","tencere","gözlemci","becerikli","cumartesi","Cem","Cenk","Can","Ece",
         "İnci","Naci","Naciye","Ecem","Ceren","Cemil","Canan","Caner","Burcu","Coşkun","Cemal","Celal","Sacit","Gonca","Cengiz","Candan","Gülcan","Cansu","Cezmi","Ceyda","Ceylin","Necati","Cennet","Cemre","Ecrin",
         "ep","pe","ap","pa","ip","pi","op","po","up","pu","üp","pü","öp","pö","ıp","pı","kap","pak","pul","pay","poz","top","küp","pas","pek","pil","piş","pus","sap","edep","cazip","depo","dolap","iplik","kapı","kupa","pamuk","para",
         "pazar","poşet","pardon","pide","ekip","çapa","deprem","karpuz","ipek","kapak","kirpik","küpe","mikrop","pasta","pano","perde","piyes","sopa","topçu","posta","püskül","rapor","şapka","otopark","kanepe","pusula",
         "palyaço","zımpara","pantolon","pencere","raptiye","süpürge","piyano","pideci","kebap","kebapçı","panayır","paraşüt","patates","patlıcan","zıpla","pazartesi","pişmaniye","şampiyon","park","pist","Sarp",
         "teyp","kulp","turp","Pelin","Alper","kapamak","Gülperi","ıspanak","papatya","Serap","pişir","pembe","patik","piknik","pekmez","Serpil","Pınar","portakal","kutup","Pakize","pırlanta","pastacı","mektup",
         "çöp","Recep","pilot","Zeynep","panda","pırasa","polis","kamp","Alp","palamut","patika","kaplan","Alpay","köpek","peynir","çap","dip","pes","pis","paşa","peki","pire","pota","çorap","kasap","kitap","köprü",
         "köpük","parça","parti","pense","çarpan","çarpım","kapat","kaptan","yaprak","cep","tıp","perşembe","toplama","Polat","tepe","Poyraz","Petek","tüp","pelerin","pergel","parmak","peçete","tepsi","spor","palto",
         "paten","patlak","paket","kirpi","maktap","sincap","pestil","pompa","köpük","yelpaze","kapalı","yap","pansuman"]

uzun=0
def hecele():
    
    uzunluk=len(tombala)

    label1=Label(text="Kalan\n"+str(uzunluk),fg='red',font=("TTKB DikTemel Abece" ,30))
   
    label1.place(relx = 0.81, rely = 0.6)

    label1=Label(text="                                                                                                                 ",fg='blue',font=("TTKB DikTemel Abece" ,80))
    
    label1.place(relx = 0.35, rely = 0.3)
    
    hecele = []
    kelime=""
    heceToplam=""
    if len(tombala) >0:
        for i in random.sample((tombala),1):
          
            kelime+=i
            bits = ''.join(['1' if l in 'AEIİOÖUÜaeıioöuü' else '0' for l in i])
            tombala.remove(i)
           
        seperators = (('101', 1),('1001', 2),('10001', 3))

        index, cut_start_pos = 0, 0

        while index < len(bits):
            for seperator_pattern, seperator_cut_pos in seperators:
                if bits[index:].startswith(seperator_pattern):
                    hecele.append(i[cut_start_pos:index + seperator_cut_pos])

                    index += seperator_cut_pos
                    cut_start_pos = index
                    break

            index += 1

        hecele.append(i[cut_start_pos:])

        for hece in hecele:
            heceToplam+=hece+" "
            
        label1=Label(text=heceToplam+" -----> "+kelime,fg='blue',font=("TTKB DikTemel Abece" ,60))
        label1.place(relx = 0.1, rely = 0.3)     

    else:
        label1=Label(text="                                                                                        ",fg='blue',font=("TTKB DikTemel Abece" ,80))
        label1.place(relx = 0.1, rely = 0.3)
        uyari=Toplevel()
        Label(uyari,text="BİTTİ. YENİLENMESİ İÇİN BAŞTAN AL BUTONUNA BASINIZ.").pack()
        uyari.mainloop()
        
def al():
        pencere.destroy()
        os.startfile("hecekelimetombala.exe")
             
pencere=Tk()
pencere.tk_setPalette("light blue")
pencere.attributes("-fullscreen", 1)

mainframe = ttk.Frame(pencere,padding='3 3 12 12')
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight =1)
                    
label=Label(text="1. - 2. - 3. - 4. GRUP (ELAKİN - OMUTÜY - ÖRIDSB - ZÇGŞCP) HECE/KELİME TOMBALASI PROGRAMI",fg="red",font=("TTKB DikTemel Abece" ,22))
label.place(relx = 0.05, rely = 0.0)

label1=Label(text="",font=("TTKB DikTemel Abece" ,60))
label1.place(relx = 0.1, rely = 0.3)

buton1=Button()
buton1.config(text="SEÇ", command=hecele,width='25',bg="red",fg="white",font=("TTKB DikTemel Abece" ,16))
buton1.place(relx = 0.08, rely = 0.85)

buton2=Button()
buton2.config(text="BAŞTAN AL", command=al,width='25',bg="red",fg="white",font=("TTKB DikTemel Abece" ,16))
buton2.place(relx = 0.40, rely = 0.85)

buton=Button()
buton.config(text="ÇIKIŞ",command=pencere.destroy,width='25',bg="red",fg="white",font=('TTKB DikTemel Abece',16))
buton.place(relx = 0.74, rely = 0.85)

pencere.mainloop()

