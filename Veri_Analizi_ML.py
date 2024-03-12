import streamlit as st


sayfa_seçenekleri = [
    "Ana Sayfa",
    "Keşifsel Veri Analizi",
    "Z Testi",
    "T Testi",
    "Basit Doğrusal Regresyon",
    "Çoklu Doğrusal Regresyon",
    "Fisher's Exact Testi",
    "Ki-Kare Testi",
    "Kruskal-Wallis Testi",
    "Wilcoxon İşaretli Sıralar Testi",
    "CART (Classification and Regression Trees)",
    "CatBoost",
    "Gaussian Naive Bayes",
    "Gradient Boosting Machines",
    "K-En Yakın Komşu (KNN)",
    "LightGBM",
    "Lojistik Regresyon",
    "Mann-Whitney U Testi",
    "Random Forest",
    "RBF SVM (Radial Basis Function Support Vector Machine)",
    "SVC (Support Vector Classification)",
    "XGBoost",
    "Yapay Sinir Ağları"
]


page = st.sidebar.selectbox("Sayfa Seçin", sayfa_seçenekleri)


if page == "Ana Sayfa":
    st.title("Veri Analizi ve Makine Öğrenimi Dünyasına Adım Atın 📈")
    
    st.subheader("Hoş Geldiniz! 🌟")
    st.write("""
             
Bu platform, veri analizi ve makine öğrenimi konularına yeni başlayanlar için tasarlanmıştır. Burada, veri odaklı kararlar almanıza yardımcı olacak temel araçları ve teknikleri öğrenme fırsatı bulacaksınız.
Başlangıç seviyesindeki kullanıcılar için hazırlanmış olan bu platform, Veri ön işleme adımları yapılmış veya basit veri setleri üzerinde yapılan işlemleri kapsar. 
             
             """)
    st.write(""" 
             Temel istatistik teknikleri, Hipotez testleri ve veri analizi yöntemlerini keşfedeceksiniz. Platformumuzda, her bir program ve algoritmanın kısa açıklamalarını içeren bir liste bulunmaktadır. Bu liste, sizin için uygun olan teknikleri belirlemenize ve keşif yolculuğunuzu daha verimli hale getirmenize yardımcı olabilir.

Hazır mısınız?🔥 Öyleyse, veri analizi ve makine öğrenimi dünyasına adım atın ve verilerinizin derinliklerine inmeye başlayın!
             
             """)
    st.write("Platformda bulunan yöntemler hakkında kısa bilgilere bir göz atalım 🧐")
    
    st.text(" ")

    st.text("""
    Makine Öğrenmesi
    Test Train Ayrımı
    Keşifsel Veri Analizi
    Basit Doğrusal Regresyon
    Çoklu Doğrusal Regresyon
    Fisher's Exact
    Ki-Kare Testi
    Kruskal Wallis Testi
    Spearman Korelasyon Katsayısı
    Pearson Korelasyon Katsayısı
    T Testi
    Wilcoxon İşaretli Sıralar Testi
    Z Testi
    CART 
    Catboost
    Gaussian Naive Bayes
    Gradient Boosting Machine
    KNN 
    LightGBM
    Lojistik Regresyon
    Mann Whitney U Testi
    Random Forest
    RBF SVC
    SVC 
    XGBoost
    Yapay Sinir Ağları

            
        
            
            """)

    headings_and_descriptions = {
        "makine öğrenmesi":"""
        Makine öğrenmesi, bilgisayar sistemlerinin veriye dayalı olarak deneyimlerden öğrenmesini ve bu deneyimlerden yararlanarak belirli görevleri gerçekleştirmesini sağlayan bir yapay zeka dalıdır. Bu algoritmalara, belirli bir görevi gerçekleştirmek için veri sağlandığında, bu veriyi analiz ederek desenleri ve ilişkileri belirleme yeteneği verilir. Bu desenler ve ilişkiler, gelecekteki benzer görevleri gerçekleştirmek için kullanılabilir.

    Makine öğrenimi genellikle denetimli, denetimsiz ve pekiştirmeli öğrenme olmak üzere üç ana kategoriye ayrılır:

    1. Denetimli Öğrenme: Bu yaklaşımda, algoritma eğitim verileriyle beslenir, her bir veri noktasının istenen çıktısı da (etiket) sağlanır. Algoritma, girişler ile çıktılar arasındaki ilişkiyi öğrenir ve yeni girişler için doğru çıktıları tahmin edebilir. Örnekler arasında sınıflandırma ve regresyon problemleri bulunur.

    2. Denetimsiz Öğrenme: Bu türde, algoritma etiketlenmemiş verilerle eğitilir, yani girişlerin etiketleri yoktur. Algoritma, veri içindeki desenleri ve ilişkileri kendi başına keşfetmeye çalışır. Örnekler arasında kümeleme ve boyut azaltma bulunur.

    3. Pekiştirmeli Öğrenme: Bu yaklaşımda, algoritma bir ortamla etkileşime girer ve belirli bir görevi en iyi şekilde gerçekleştirmek için çeşitli adımlar atar. Algoritma, yaptığı adımların sonuçlarına göre bir ödül veya ceza alır ve bu geri bildirimleri kullanarak en iyi eylem stratejilerini öğrenir. Örnekler arasında oyun teorisi ve robotik kontrol bulunur.

    Makine öğrenimi, birçok farklı alanı etkilemiştir ve otomatik görüntü tanıma, doğal dil işleme, tıbbi teşhis, finansal tahminler ve daha birçok alanda kullanılmaktadır.""",
        "test train ayrımı":"""
        Test-train ayrımı, makine öğrenimi ve istatistiksel modelleme süreçlerinde yaygın olarak kullanılan bir kavramdır. Bu kavram, bir modelin eğitilmesi ve performansının değerlendirilmesi için veri setinin bölünmesini ifade eder.

    Genellikle veri seti iki ana bölüme ayrılır:

    1. Eğitim Seti (Train Set): Modelin eğitilmesi için kullanılan veri setidir. Bu veri seti, modelin giriş-veri ilişkilerini öğrenmesi için kullanılır. Model, eğitim veri setindeki örneklerden desenler ve ilişkiler çıkararak belirli bir görevi gerçekleştirebilecek şekilde ayarlanır.

    2. Test Seti (Test Set): Modelin performansını değerlendirmek için kullanılan bağımsız bir veri setidir. Model eğitildikten sonra, test veri setindeki örnekleri kullanarak modelin doğruluğunu, hassasiyetini ve genel performansını değerlendiririz. Bu, modelin eğitim sırasında görmediği veriler üzerinde nasıl performans gösterdiğini belirlemek için yapılır. 

    Test-train ayrımı, modelin gerçek dünya verileri üzerinde ne kadar iyi performans gösterebileceğini daha güvenilir bir şekilde ölçmek için kullanılır. Ayrıca, aşırı uyum (overfitting) gibi problemlerin tespit edilmesine ve düzeltilmesine yardımcı olur. Bu yaklaşım, modelin genelleme yeteneğini test etmek için önemlidir; yani, eğitim veri setinden öğrendiği desenleri, yeni ve görülmemiş veri setlerine genellemesini sağlamak için kullanılır.
        """,
        
        "keşifsel veri analizi": """Keşifsel veri analizi (EDA), veri bilimi ve istatistikte, bir veri setinin doğasını ve yapısını anlamak için kullanılan bir süreçtir. EDA, veri setindeki desenleri, ilişkileri, anormallikleri ve potansiyel sorunları keşfetmek için çeşitli görselleştirme ve istatistiksel teknikler kullanır.

    EDA'nın temel amaçları şunlardır:

    1. **Veri setinin Yapısını Anlama**: Veri setindeki değişkenlerin türünü, dağılımını ve ilişkilerini anlamak için yapısal özelliklerini incelemek.

    2. **Desenleri ve İlişkileri Belirleme**: Veri setindeki desenleri, ilişkileri ve trendleri belirlemek için grafikler, tablolar ve istatistiksel metotlar kullanarak veriye göz atmaktır.

    3. **Anormallikleri ve Sorunları Tespit Etme**: Veri setindeki eksik değerler, aykırı değerler, yanlış veri girişleri gibi sorunları belirlemek ve bunları çözmek için stratejiler geliştirmek.

    4. **Varsayımları Test Etme**: İleri analiz ve modelleme için varsayımların geçerliliğini kontrol etmek.

    5. **Modelleme Stratejileri Geliştirme**: Veri setindeki desenleri ve ilişkileri anlayarak, daha sonraki analizler veya modelleme işlemleri için uygun stratejiler geliştirmek.

    EDA, veri bilimcilerin ve analistlerin veri setlerini anlamalarına, modelleme sürecine hazırlanmalarına ve doğru analiz yöntemlerini seçmelerine yardımcı olur. Bu nedenle, veri analizi sürecinin önemli bir adımıdır ve veri tabanlı karar alma sürecinde kritik bir rol oynar.
        
        
        """,
        "basit doğrusal regresyon": """
        Basit doğrusal regresyon, istatistik ve makine öğrenimi alanlarında kullanılan temel bir regresyon analizi yöntemidir. Bu yöntem, bağımlı değişken ile bir tane bağımsız değişken arasındaki ilişkiyi modellemek için kullanılır.

    Basit doğrusal regresyon modeli, genellikle şu formül ile ifade edilir:

    y= β0 + β1X + ϵ

    Burada:

    - Y: Bağımlı değişkeni temsil eder.
    - X: Bağımsız değişkeni temsil eder.
    - β0: Doğrunun y-eksenini kestiği yer ve regresyon sabitidir.
    - β1: Doğrunun eğimi veya regresyon katsayısıdır.
    - ϵ: hata terimini ifade eder.

    Basit doğrusal regresyon, bağımlı değişkenin ve bağımsız değişkenin doğrusal bir ilişki içinde olduğu durumlar için uygundur. Örneğin, bir kişinin boyu (bağımlı değişken) ile kilosu (bağımsız değişken) arasındaki ilişkiyi modellemek için kullanılabilir.

    Model eğitilirken, regresyon katsayıları β0 ve β1 genellikle en küçük kareler yöntemiyle tahmin edilir. Bu, hatanın karelerinin toplamını (residual sum of squares) minimize eden katsayıların bulunması anlamına gelir.

    Basit doğrusal regresyon analizi, modelin uygunluğunu değerlendirmek için çeşitli istatistiksel metrikler kullanır. Bu metrikler arasında R-kare (R-squared), ortalamadan sapma karelerinin (mean squared error) karekökü ve diğerleri bulunur. Bu metrikler, modelin ne kadar iyi uyum sağladığını ve bağımsız değişkenin bağımlı değişkendeki değişikliği ne kadar iyi açıkladığını değerlendirmek için kullanılır.
        
        
        """,
        "çoklu doğrusal regresyon": """
        Çoklu doğrusal regresyon, bir bağımlı değişken ile birden fazla bağımsız değişken arasındaki ilişkiyi modellemek için kullanılan bir regresyon analizi yöntemidir. Basit doğrusal regresyon ile benzer bir prensibe sahiptir, ancak birden fazla bağımsız değişkeni içerir.

    Genel olarak, çoklu doğrusal regresyon modeli aşağıdaki şekilde ifade edilir:

    Yi = β0 + β1X1 + β2X2 + ……+ βnXn  + €i 

    Burada:

    - Y: Bağımlı değişkeni temsil eder.
    - X1,X2,,Xn: Modeldeki bağımsız değişkenleri temsil eder.
    - β0,β1,β2,,βn: regresyon katsayılarını temsil eder. β0 sabit terimi (intercept), β1,β2,,βn ise her bir bağımsız değişkenin eğimini (slope) ifade eder.
    - €: Hata terimini ifade eder.

    Çoklu doğrusal regresyon, bağımlı değişken ile birden fazla bağımsız değişken arasındaki ilişkiyi açıklamak ve tahmin etmek için kullanılır. Örneğin, bir aracın fiyatını (bağımlı değişken) belirleyen faktörleri incelemek istediğimizi düşünelim. Bu durumda aracın yaşını, kilometre durumunu, motor gücünü, yakıt tüketimini ve diğer özelliklerini bağımsız değişkenler olarak kullanarak fiyatı tahmin etmeye çalışabiliriz.

    Çoklu doğrusal regresyon analizi, her bir bağımsız değişkenin bağımlı değişkendeki varyansı açıklamadaki katkısını değerlendirmek için kullanılır. Ayrıca, modelin uygunluğunu değerlendirmek ve istatistiksel olarak anlamlı değişkenleri belirlemek için çeşitli istatistiksel testler kullanılır.
        
        """,
        
        "fisher's exact": """
        Fisher'ın kesin testi (Fisher's exact test), küçük örneklemler veya düşük hücre sayısı durumlarında kullanılan bir istatistiksel testtir. Özellikle 2x2 veya daha küçük tablolarda gözlenen frekanslar arasındaki ilişkiyi test etmek için yaygın olarak kullanılır.

    Fisher'ın kesin testi, birçok diğer istatistiksel testten farklı olarak, varsayımlara dayanmaz. Bu nedenle, örneklemin büyüklüğünden bağımsız olarak güvenilir sonuçlar üretebilir. Özellikle küçük örneklemler veya nadir olayların incelendiği durumlarda tercih edilir.

    Fisher'ın kesin testi genellikle kategorik verilerin analizi için kullanılır. Örneğin, bir tedavi ve kontrol grubu arasındaki başarı oranları, hastalık varlığı ve yokluğu ile belirli bir genin ilişkisi gibi durumlarda kullanılabilir.

    Fisher'ın kesin testinin temel amacı, iki kategorik değişken arasındaki ilişkiyi test etmektir. Testin null hipotezi, iki değişken arasında bir ilişkinin olmadığını ifade eder. Alternatif hipotez ise, iki değişken arasında bir ilişki olduğunu öne sürer.

    Fisher'ın kesin testi, örneklem verilerini kullanarak bir p-değeri hesaplar. Bu p-değeri, null hipotezin reddedilmesi için sağlanan kanıttır. Eğer p-değeri belirli bir alfa düzeyinden (genellikle 0.05 veya 0.01) daha küçükse, null hipotez reddedilir ve iki değişken arasında anlamlı bir ilişki olduğu sonucuna varılır.
        """,
        
        "ki-kare testi": """
        Ki-kare testi, iki kategorik değişken arasındaki ilişkinin anlamlılığını test etmek için kullanılan bir istatistiksel testtir. Bu test, gözlenen ve beklenen frekanslar arasındaki farklılıkları değerlendirerek değişkenler arasındaki ilişkiyi belirler.

    Ki-kare testi, özellikle nominal ölçek düzeyindeki verilerin analizi için uygundur. Örneğin, iki kategorik değişken arasındaki ilişkiyi test etmek için kullanılabilir, örneğin, sigara içme alışkanlığı ile cinsiyet arasındaki ilişkiyi belirlemek gibi.

    Ki-kare testinin temel adımları şunlardır:

    1. **Gözlenen Frekansların Belirlenmesi**: İlk olarak, analiz edilen veri setindeki gözlenen frekanslar belirlenir. Bu, her bir kategorinin kaç kez gözlemlendiğinin sayılması anlamına gelir.

    2. **Beklenen Frekansların Hesaplanması**: İkinci adımda, bağımsız değişkenlerin birbirine bağlı olmaması durumunda beklenen frekanslar hesaplanır. Bu, toplam örnek sayısının ve her bir kategorinin marjinal dağılımının kullanılmasıyla yapılır.

    3. **Ki-kare İstatistiğinin Hesaplanması**: Gözlenen ve beklenen frekanslar arasındaki farkları ölçmek için ki-kare istatistiği hesaplanır. Bu, gözlenen frekanslar ile beklenen frekanslar arasındaki farkların karelerinin toplamının, beklenen frekanslara oranlanarak hesaplanır.

    4. **P-değeri Hesaplanması**: Elde edilen ki-kare istatistiği kullanılarak p-değeri hesaplanır. Bu p-değeri, null hipotezinin (iki değişken arasında bir ilişki olmadığı hipotezi) reddedilmesi için sağlanan kanıttır. 

    5. **Sonuçların Yorumlanması**: Elde edilen p-değerinin belirlenen alfa düzeyinden (genellikle 0.05 veya 0.01) daha küçük olması durumunda, null hipotez reddedilir ve değişkenler arasında anlamlı bir ilişki olduğu sonucuna varılır. Ancak, p-değeri belirli bir alfa düzeyinden büyükse, null hipotezi reddedilmez ve değişkenler arasında anlamlı bir ilişki olmadığı sonucuna varılır.

    Ki-kare testi, ilişkiyi değerlendirmenin yanı sıra, kategorik verilerin homojenlik veya bağımsızlık gibi diğer özelliklerini test etmek için de kullanılabilir.
        
        """,
        
        "kruskal wallis testi": """
        Kruskal-Wallis testi, gruplar arasındaki merkezi eğilimlerin (ortalama, medyan vb.) eşit olup olmadığını belirlemek için kullanılan bir non-parametrik istatistik testidir. Bu test, gruplar arasındaki farklılıkları değerlendirmek için kullanılır ve gruplar normal dağılımı sağlamadığında veya gruplar arasındaki varyans homojenliği varsayımı sağlanmadığında tercih edilir.

    Kruskal-Wallis testi, grupların ortanca değerlerini karşılaştırır. Gruplar arasında anlamlı bir fark olup olmadığını belirlemek için sıralı veriler kullanılır. Bu test, iki grup arasındaki farklılıkları değil, üç veya daha fazla grup arasındaki farklılıkları değerlendirir.

    Kruskal-Wallis testinin null hipotezi, tüm grupların popülasyon dağılımında ortanca değerlerinin eşit olduğunu ifade eder. Alternatif hipotez ise, en az bir grup ortancasının diğerlerinden farklı olduğunu öne sürer.

    Kruskal-Wallis testi, öncelikle sıralı verilerle çalışır. Veriler sıralanır ve her bir gözlem, sıralandığı konumunu belirtir. Daha sonra, her grup için sıralı değerlerin toplamı hesaplanır. Bu toplamların kullanılmasıyla bir test istatistiği hesaplanır.

    Elde edilen test istatistiği, Kruskal-Wallis dağılımı altında bir p-değeri hesaplanması için kullanılır. Bu p-değeri, null hipotezin reddedilmesi için sağlanan kanıttır. Eğer p-değeri belirlenen alfa düzeyinden (genellikle 0.05 veya 0.01) daha küçükse, null hipotez reddedilir ve en az bir grup ortancasının diğerlerinden farklı olduğu sonucuna varılır. Ancak, p-değeri belirlenen alfa düzeyinden büyükse, null hipotez reddedilmez ve gruplar arasında anlamlı bir fark olmadığı sonucuna varılır.

    Kruskal-Wallis testi, özellikle grupların normal dağılımı sağlamadığı veya varyans homojenliği varsayımının sağlanmadığı durumlarda tercih edilir. Bu nedenle, parametrik testlerin varsayımlarının sağlanmadığı durumlarda kullanışlı bir alternatif sunar.
        
        """,
        
        "spearman korelasyon katsayısı": """
        Spearman korelasyon katsayısı, iki değişken arasındaki ilişkinin gücünü ve yönünü ölçmek için kullanılan bir istatistiksel yöntemdir. Özellikle, iki değişken arasındaki ilişki monotonic (sürekli artan veya azalan) ancak lineer olmayan bir ilişki olduğunda kullanılır.

    Spearman korelasyon katsayısı, Pearson korelasyon katsayısına benzer bir şekilde -1 ile +1 arasında değer alır. Ancak, Pearson korelasyon katsayısı, değişkenler arasındaki lineer ilişkiyi ölçerken, Spearman korelasyon katsayısı, değişkenler arasındaki monotonic ilişkiyi ölçer.

    Spearman korelasyon katsayısının hesaplanması için şu adımlar izlenir:

    1. İlk olarak, her bir değişkenin değerleri sıralanır. Eğer iki değişkenin aynı değere sahip birden fazla gözlemi varsa, bu gözlemler rastgele sıralanır.

    2. Ardından, her bir gözlem için sıralar arasındaki farklar hesaplanır. Bu farklar, bir değişkenin sıralama pozisyonundan diğer değişkenin sıralama pozisyonu çıkarılarak bulunur.

    3. Son olarak, sıralar arasındaki farkların Pearson korelasyon katsayısı hesaplanır. Bu, sıralar arasındaki farkların Pearson korelasyon katsayısının hesaplanması için kullanılmasına dayanır.

    Spearman korelasyon katsayısı, değişkenler arasındaki ilişkinin gücünü ve yönünü değerlendirmek için kullanılır. Özellikle, veri normal dağılıma sahip değilse veya aykırı değerler varsa tercih edilir. Ayrıca, değişkenler arasındaki ilişkinin doğrusal olmadığı durumlarda da kullanışlıdır.
        """,
        
        "pearson korelasyon katsayısı": """
        Pearson korelasyon katsayısı, iki değişken arasındaki ilişkinin gücünü ve yönünü ölçmek için kullanılan bir istatistiksel yöntemdir. Bu katsayı, değişkenler arasındaki doğrusal ilişkiyi ifade eder.

    Pearson korelasyon katsayısı, genellikle "-1" ile "+1" arasında bir değer alır:

    - +1: Mükemmel pozitif ilişki. Bu, iki değişken arasında tam bir doğrusal ilişki olduğunu gösterir. Bir değişken artarken, diğer değişken de artar.
    - 0: İlişki yoktur. İki değişken arasında herhangi bir ilişki bulunmamaktadır.
    - -1: Mükemmel negatif ilişki. Bu, iki değişken arasında tam ters yönlü bir doğrusal ilişki olduğunu gösterir. Bir değişken artarken, diğer değişken azalır.

    Pearson korelasyon katsayısı, iki değişken arasındaki ilişkiyi doğrusal olarak modellemek için kullanılır. Örneğin, bir değişkenin diğer değişkeni ne kadar iyi tahmin edebileceğini veya iki değişkenin birlikte nasıl değiştiğini belirlemek için kullanılabilir.

    Pearson korelasyon katsayısının hesaplanması için şu adımlar izlenir:

    1. İlk olarak, iki değişken arasındaki ilişkinin gücünü ve yönünü ölçmek için bir kovaryans hesaplanır.

    2. Ardından, her bir değişkenin standart sapması hesaplanır.

    3. Son olarak, kovaryans, iki değişkenin standart sapmalarının çarpımına bölünerek Pearson korelasyon katsayısı elde edilir.

    Pearson korelasyon katsayısı, genellikle birçok alanda kullanılır, özellikle istatistik, bilim, mühendislik ve sosyal bilimlerde. Ancak, iki değişken arasındaki ilişki doğrusal değilse veya veri normal dağılıma sahip değilse, diğer korelasyon yöntemleri (örneğin, Spearman korelasyon katsayısı) kullanılabilir.
        """,
        
        "t testi": """
        T-testi, bir grup ortalaması arasındaki farkın anlamlılığını test etmek için kullanılan istatistiksel bir testtir. T-testi, bir grup ile bir diğer grup arasında ortalamalar arasında bir fark olup olmadığını belirlemek için kullanılır.

    T-testi genellikle iki durumda kullanılır:

    1. Bağımsız İki Örneklem T-testi: İki bağımsız grup arasında ortalamalar arasındaki farkı test etmek için kullanılır. Örneğin, bir tedavi grubu ile kontrol grubu arasında bir tedavinin etkisini değerlendirmek için kullanılabilir.

    2. Eşleştirilmiş İki Örneklem T-testi: İki grup arasında eşleştirilmiş örnekler varsa ve ortalamalar arasındaki farkı test etmek istiyorsak kullanılır. Bu, aynı kişilerin veya birimlerin iki farklı koşul altında alınan ölçümlerini karşılaştırmak için kullanışlıdır.

    T-testi, genellikle parametrik bir test olarak kabul edilir, yani belirli varsayımlar altında çalışır:

    - Değişkenler normal dağılıma sahip olmalıdır.
    - Değişkenler homojen varyansa sahip olmalıdır (grupların varyansları benzer olmalıdır).

    T-testi sonucunda elde edilen istatistiksel sonuçlar, gruplar arasındaki farklılıkların anlamlılığını değerlendirmek için kullanılır. Eğer p-değeri belirli bir alfa düzeyinden (genellikle 0.05 veya 0.01) daha küçükse, null hipotez reddedilir ve gruplar arasında anlamlı bir fark olduğu sonucuna varılır. Ancak, p-değeri belirlenen alfa düzeyinden büyükse, null hipotez reddedilmez ve gruplar arasında anlamlı bir fark olmadığı sonucuna varılır.
        """,
        
        "wilcoxon işaretli sıralar testi": """
        Wilcoxon işaretli sıralar testi, eşleştirilmiş örnekler üzerindeki medyan farkının anlamlılığını test etmek için kullanılan bir non-parametrik istatistik testidir. İki durum arasında farkın medyan değerine dayalı olarak değerlendirilmesini sağlar. Özellikle, veri normal dağılıma sahip değilse veya varyans homojenliği varsayımı sağlanmadığında tercih edilir.

    Wilcoxon işaretli sıralar testi, eşleştirilmiş örneklerin sıralı değerlerini kullanarak çalışır. İlk olarak, iki durum arasındaki farklar (farklı koşullar altında alınan ölçümler) hesaplanır. Ardından, bu farklar sıralanır ve mutlak değerleri alınır. Sıralı mutlak değerler üzerindeki işaretler (pozitif veya negatif) korunur. Son olarak, sıralı mutlak değerlerin işaretli sıraları toplanır ve test istatistiği hesaplanır.

    Wilcoxon işaretli sıralar testi, verilerin normal dağılıma sahip olmadığı veya parametrik testlerin varsayımlarının sağlanmadığı durumlarda tercih edilir. Özellikle, eşleştirilmiş örnekler üzerindeki ortalamaların veya medyanların farklı olup olmadığını belirlemek için kullanılır.

    Wilcoxon işaretli sıralar testinin null hipotezi, iki durum arasında medyan farkının olmadığını ifade eder. Alternatif hipotez ise, iki durum arasında medyan farkının olduğunu öne sürer. Test sonucunda elde edilen p-değeri, null hipotezin reddedilmesi için sağlanan kanıttır. Eğer p-değeri belirli bir alfa düzeyinden (genellikle 0.05 veya 0.01) daha küçükse, null hipotez reddedilir ve iki durum arasında anlamlı bir medyan farkı olduğu sonucuna varılır. Ancak, p-değeri belirlenen alfa düzeyinden büyükse, null hipotez reddedilmez ve iki durum arasında anlamlı bir medyan farkı olmadığı sonucuna varılır.
        """,
        
        "z testi": """
        Z-testi, bir popülasyon parametresi hakkında yapılan bir önermenin doğruluğunu test etmek için kullanılan bir istatistiksel testtir. Özellikle, popülasyon ortalaması veya oranı gibi parametreler hakkında önermeleri test etmek için kullanılır.

    Z-testi, örneklemlerden elde edilen verilere dayanarak popülasyon hakkında bir önermenin doğruluğunu değerlendirir. Bu test, genellikle büyük örneklem boyutları veya popülasyon standart sapması bilindiğinde kullanılır.

    Z-testi, örneklem verilerinin standart hata ile standart normal dağılıma göre standart sapma kullanılarak bir z-puanına dönüştürülmesini içerir. Bu z-puanı, örneklem verilerine dayalı olarak popülasyon parametresinin önerilen değeri ile karşılaştırılır.

    Z-testinin temel adımları şunlardır:

    1. Null ve alternatif hipotezlerin belirlenmesi: Test edilmek istenen önermeleri belirler.

    2. Test istatistiğinin hesaplanması: Örneklem verilerine dayalı olarak bir test istatistiği hesaplanır. Bu istatistik, popülasyon parametresinin önerilen değeri ile karşılaştırılır.

    3. P-değeri hesaplanması: Elde edilen test istatistiği kullanılarak bir p-değeri hesaplanır. Bu p-değeri, null hipotezin reddedilmesi için sağlanan kanıttır.

    4. Sonuçların yorumlanması: Elde edilen p-değeri belirlenen alfa düzeyinden (genellikle 0.05 veya 0.01) daha küçükse, null hipotez reddedilir ve alternatif hipotez kabul edilir. Ancak, p-değeri belirlenen alfa düzeyinden büyükse, null hipotez reddedilmez ve alternatif hipotez kabul edilmez.

    Z-testi, özellikle büyük örneklem boyutları veya popülasyon standart sapması bilindiğinde parametrik bir test olarak kullanılabilir. Öte yandan, küçük örneklem boyutları veya popülasyon standart sapması bilinmediğinde, t-testi gibi alternatif non-parametrik testler tercih edilebilir.
        """,
        
        "cart": """
        CART (Classification and Regression Trees), sınıflandırma ve regresyon için kullanılan bir ağaç yapısıdır. Bu yöntem, veri kümesindeki ilişkileri belirlemek ve örüntüleri tanımlamak için kullanılır. Sınıflandırma ağaçları, kategorik hedef değişkenlerini tahmin etmek için kullanılırken, regresyon ağaçları sürekli hedef değişkenlerini tahmin etmek için kullanılır.

    CART algoritması, ağaç yapısını oluştururken veri kümesindeki en iyi bölünmeyi belirlemek için bir dizi karar kuralı kullanır. Her bir bölünme, veri kümesini homojen alt gruplara böler. Bu bölünmeler, veri kümesindeki örüntüleri daha iyi açıklamak için bir dizi karar kuralı kullanılarak tekrar tekrar uygulanır. Sonuç olarak, bir ağaç oluşturulur; bu ağaç, veri kümesindeki örüntüleri görsel olarak temsil eder ve hedef değişkenin tahmin edilmesine olanak sağlar.

    Sınıflandırma ağaçları, bir sınıflandırma problemindeki sınıfları veya kategorik hedef değişkenleri tahmin etmek için kullanılır. Örneğin, bir kişinin kredi başvurusunun onaylanıp onaylanmayacağını tahmin etmek gibi. Regresyon ağaçları ise, bir regresyon problemi için sürekli hedef değişkenlerini tahmin etmek için kullanılır. Örneğin, bir evin fiyatını tahmin etmek gibi.

    CART algoritması, basit, esnek ve yüksek performanslı bir model oluşturmak için yaygın olarak kullanılır. Ayrıca, ağaç yapısının yorumlanması kolaydır, bu nedenle karar ağaçlarını analiz etmek ve sonuçlarını yorumlamak oldukça sezgiseldir.
        """,
        
        "catboost": """
        CatBoost, kategorik değişkenleri etkili bir şekilde ele alan bir gradient boosting çerçevesidir. Gradient boosting, zayıf öğrenicileri (genellikle karar ağaçları) bir araya getirerek güçlü bir öğrenici oluşturan bir makine öğrenimi tekniğidir. CatBoost, kategorik değişkenleri otomatik olarak işler ve bu nedenle veri setindeki kategorik değişkenlerin dönüştürülmesi veya kodlanması gerekmez.

    CatBoost, performansı artırmak için bir dizi yenilikçi teknik kullanır. Örneğin, asimetrik ağaç büyümesi, bağlam duyarlı hücre seçimi ve dinamik öğrenme oranı gibi teknikler kullanarak ağaçların oluşturulmasını optimize eder. Ayrıca, CatBoost, genellikle overfittingi önlemek için kullanılan bir dizi düzenleme tekniği de içerir.

    CatBoost, büyük ölçekli veri setleri üzerinde yüksek performans gösterir ve genellikle sıralama, sınıflandırma ve regresyon gibi çeşitli makine öğrenimi problemlerinde başarılı sonuçlar verir. Ayrıca, CatBoost, Python, R, C++ gibi yaygın programlama dillerinde kullanılabilir ve açık kaynaklı bir projedir.
        
        """,
        
        "gaussian naive bayes": """
        Gaussian Naive Bayes, Naive Bayes sınıflandırma algoritmasının bir türüdür ve özellikle sürekli özelliklere sahip veri setleriyle çalışır. Naive Bayes sınıflandırma algoritmaları, Bayes teoremini kullanarak sınıflandırma yaparlar. Gaussian Naive Bayes, sınıflandırma problemlerini çözmek için normal (Gaussian) dağılımı varsayarak çalışır.

    Gaussian Naive Bayes algoritması, her sınıf için veri setindeki her özelliğin normal dağıldığını varsayar. Bu, her özellik için ortalama ve standart sapmanın hesaplanmasını gerektirir. Ardından, veri noktasının her bir özelliği için normal dağılım yoğunluk fonksiyonları kullanılarak sınıf etiketi belirlenir.

    Gaussian Naive Bayes'in "naive" (saf) olarak adlandırılmasının nedeni, özellikler arasındaki bağımsızlık varsayımıdır. Bu, her özelliğin sınıf etiketi üzerindeki etkisinin birbirinden bağımsız olduğu anlamına gelir. Bu varsayım gerçekte nadiren tam olarak doğrudur, ancak Naive Bayes algoritmaları genellikle pratikte iyi performans gösterirler.

    Gaussian Naive Bayes, özellikle küçük boyutlu veri setleri veya yüksek boyutlu özellik uzaylarıyla çalışırken etkilidir. Ayrıca, kategorik veya nominal veri ile birlikte sürekli veri kullanımına izin verir. Bununla birlikte, veri seti üzerinde bazı varsayımların doğru olmadığı durumlarda performansı düşebilir.
        
        """,
        
        "gradient boosting machine": """
        Gradient Boosting Machine (GBM), bir makine öğrenimi tekniği olan Gradient Boosting'in uygulanmasıyla oluşturulan bir modeldir. Gradient Boosting, zayıf tahmin edicilerin (genellikle karar ağaçları) bir araya getirilerek güçlü bir tahmin edici oluşturulmasına dayanan bir ensemble yöntemidir. Gradient Boosting Machine, bu tekniği kullanarak karmaşık ilişkileri modellemek için kullanılan bir modeldir.

    Gradient Boosting Machine, temel olarak aşağıdaki adımları takip eder:

    1. **İlk Tahminin Oluşturulması:** İlk tahmin olarak basit bir model kullanılır. Genellikle veri setindeki ortalama değer veya sabit bir tahmin değeri kullanılabilir.

    2. **Hata (Artık) Hesaplama:** İlk tahmin ile gerçek değerler arasındaki farklar, modelin hata (artık) değerleri olarak hesaplanır.

    3. **Hata Tabanlı Yeni Tahminlerin Oluşturulması:** Bir sonraki aşamada, hata değerlerini tahmin etmek için yeni bir model oluşturulur. Bu, hataların tahmin edilmesini sağlar ve böylece daha iyi tahminler elde etmek için kullanılır.

    4. **Yeni Tahminlerin Entegrasyonu:** Yeni tahminler, önceki tahminlere eklenerek birleştirilir. Bu, modelin doğruluğunu artırmak için kullanılır.

    5. **Yeni Modelin Hata Analizi ve Sürecin Tekrarlanması:** Yeni modelin hata analizi yapılır ve hataların bir sonraki model için kullanılmasıyla süreç tekrarlanır. Bu adımlar, bir dizi tahmin edici oluşturulana kadar devam eder.

    Gradient Boosting Machine, karmaşık ilişkileri modellemek ve yüksek doğruluklu tahminler yapmak için etkili bir yöntemdir. Özellikle sınıflandırma ve regresyon problemlerinde başarılı sonuçlar verir. Gradient Boosting Machine, aynı zamanda özelliklerin önem sıralamasını elde etmek için de kullanılabilir, böylece hangi özelliklerin modelin performansını etkilediği anlaşılabilir.
        """,
        
        "knn": """K-Nearest Neighbors (KNN), temel bir sınıflandırma ve regresyon algoritmasıdır. KNN, örneklerin birbirine olan benzerliklerine dayalı olarak sınıflandırma veya tahmin yapar. Özellikle basit, etkili ve kolay anlaşılabilir bir algoritmadır.

    KNN algoritması şu adımları izler:

    1. **Örneklerin Benzerliklerinin Hesaplanması:** KNN, örnekler arasındaki benzerlikleri ölçmek için genellikle Öklid mesafesi veya diğer benzer mesafe metriklerini kullanır.

    2. **K En Yakın Komşuların Belirlenmesi:** Verilen bir örnek için, KNN algoritması en yakın k komşuyu belirler. Bu komşular, verilen örneğe en yakın olan K örnektir.

    3. **Sınıflandırma veya Tahmin Yapılması:** Sınıflandırma problemleri için, KNN sadece K en yakın komşuların etiketlerine bakar ve çoğunluk sınıfının etiketini tahmin olarak kullanır. Örneğin, eğer K = 3 ise ve bu 3 komşudan 2'si "mavi" etiketine sahipse, tahmin "mavi" olacaktır. Regresyon problemleri için, KNN K en yakın komşunun ortalamasını veya ağırlıklı ortalamasını kullanarak tahmin yapar.

    KNN algoritması, eğitim süresi boyunca bir model oluşturmaz; bunun yerine, eğitim verilerini bellekte saklar ve tahmin yapmak için bu verilere doğrudan başvurur. Bu, modelin eğitim sürecinin hızlı olmasını sağlar, ancak tahmin yapmak için gerçek zamanlı veriye erişim gerektirir.

    KNN'nin bir dezavantajı, tahmin yapmak için tüm eğitim verilerini bellekte saklamasıdır, bu da büyük veri setlerinde bellek ve hesaplama kaynaklarının hızla tükenmesine neden olabilir. Ayrıca, K değerinin (komşu sayısı) doğru bir şekilde seçilmesi önemlidir; yanlış bir K değeri modelin performansını olumsuz yönde etkileyebilir.""",
        
        "lightgbm": """
        LightGBM (Light Gradient Boosting Machine), büyük veri setlerinde yüksek performanslı ve dağıtılmış bir gradient boosting çerçevesidir. LightGBM, Microsoft tarafından geliştirilen ve açık kaynaklı olarak yayınlanan bir makine öğrenimi kütüphanesidir. 

    LightGBM, diğer gradient boosting kütüphanelerine kıyasla çeşitli yenilikçi teknikler kullanarak hız ve performans avantajları sağlar. Bu teknikler arasında özellikle özellik parçacıklandırma, eksik değerlerin işlenmesi, katmanlı karar ağaçları ve daha efektif histogram hesaplama yöntemleri bulunmaktadır.

    LightGBM, büyük ölçekli veri setlerinde yüksek performans gösterir ve genellikle sınıflandırma, regresyon ve sıralama gibi çeşitli makine öğrenimi problemlerinde kullanılır. Ayrıca, LightGBM, CPU ve GPU üzerinde çalışabilir, bu da işlem gücünü artırarak model eğitim süresini optimize eder.

    LightGBM, kullanımı kolay bir API sağlar ve Python, R, Java, C++ gibi çeşitli programlama dillerinde kullanılabilir. Özellikle büyük veri setleri üzerinde yüksek performanslı makine öğrenimi uygulamaları geliştirmek isteyenler için popüler bir tercihtir.
        """,
        
        "lojistik regresyon": """
        Lojistik regresyon, bir sınıflandırma algoritmasıdır ve birçok makine öğrenimi probleminde kullanılır. Özellikle, iki sınıf arasında sınıflandırma yapmak için kullanılır (binary sınıflandırma). Örneğin, bir müşterinin bir ürünü satın alıp almama olasılığını tahmin etmek gibi.

    Lojistik regresyon, bir sigmoid fonksiyonu olarak adlandırılan özel bir aktivasyon fonksiyonu kullanır. Bu sigmoid fonksiyonu, herhangi bir gerçek sayıyı 0 ile 1 arasında bir değere dönüştürür ve sonuç olarak bir olasılık değeri verir. Lojistik regresyon modeli, girdi özelliklerinin ağırlıklarını ve bir sapmayı (bias) kullanarak bir doğrusal kombinasyon oluşturur ve bu kombinasyonu sigmoid fonksiyonuna geçirerek sonuç olarak bir olasılık değeri elde eder.

    Lojistik regresyonun temel adımları şunlardır:

    1. **Model Kurma:** Öncelikle, veri seti üzerinde bir lojistik regresyon modeli kurulur. Bu, girdi özelliklerinin ağırlıklarının belirlenmesini ve bir sapmanın hesaplanmasını içerir.

    2. **Eğitim:** Model, veri setindeki örneklerle eğitilir. Bu, modelin parametrelerinin (ağırlıklar ve sapma) optimize edilmesini sağlar.

    3. **Tahmin Yapma:** Eğitim tamamlandıktan sonra, model test veri seti üzerinde kullanılarak tahminler yapabilir. Sigmoid fonksiyonuna giren doğrusal kombinasyon, sınıf etiketinin olasılığı olarak yorumlanabilir.

    Lojistik regresyon, basit, yorumlanabilir ve hesaplama açısından hızlıdır. Ayrıca, sınıflandırma problemleri için geniş bir uygulama alanına sahiptir ve özellikle binary sınıflandırma problemlerinde yaygın olarak kullanılır.
        """,
        
        "mann whitney u testi": """Mann-Whitney U testi, iki bağımsız örneklem grubu arasında ortalamalar arasında anlamlı bir fark olup olmadığını belirlemek için kullanılan bir non-parametrik istatistik testidir. Özellikle, gruplar normal dağılıma sahip değilse veya varyans homojenliği varsayımı sağlanmadığında tercih edilir.

    Mann-Whitney U testi, örneklemlerdeki sıralı verilerin kullanılmasına dayanır. İki grup arasındaki medyan farkını karşılaştırır ve bu farkın rastgele olup olmadığını değerlendirir. Bu test, gruplardaki sıralı verilerin toplam sıraları arasındaki farkı kullanarak çalışır.

    Mann-Whitney U testi, aşağıdaki adımları izler:

    1. **Örneklerin Birleştirilmesi:** İki bağımsız örneklem grubu birleştirilir ve sıralanır.

    2. **Sıralı Verilere Göre Rütbelerin Atanması:** Birleştirilmiş örneklemlere sıralı olarak rütbeler atanır. Eşit değerler için ortalamalar kullanılır.

    3. **Toplam Rütbe İstatistiğinin Hesaplanması:** Her grubun toplam rütbesi hesaplanır. Bu, her grup için sıralı verilerin toplam sıralarının kullanılmasıyla yapılır.

    4. **U İstatistiğinin Hesaplanması:** Grupların toplam rütbeleri arasındaki fark olan U istatistiği hesaplanır.

    5. **Kritik Değerler veya p-değeri ile Karşılaştırma:** Hesaplanan U istatistiği, tablo değerleri veya p-değeri ile karşılaştırılarak gruplar arasındaki farkın anlamlı olup olmadığı belirlenir.

    Mann-Whitney U testi, parametrik olmayan bir test olduğu için belirli varsayımlar gerektirmez. Bu nedenle, verilerin dağılımı veya varyans homojenliği gibi ön koşullar sağlanmadığında bile güvenle kullanılabilir. Bu test, gruplar arasındaki merkezi eğilim farklarını belirlemek için yaygın olarak kullanılır.""",
        
        "random forest": """
        Random Forest, ensemble öğrenme yöntemlerinden biridir ve sınıflandırma ve regresyon problemlerinde kullanılır. Birçok karar ağacının bir araya getirilmesiyle oluşturulan güçlü bir modeldir. 

    Random Forest algoritması şu adımları takip eder:

    1. **Rastgele Alt-Örneklerin Oluşturulması:** Veri seti üzerinde rastgele bir alt-örneklem seçilir (bagging).

    2. **Karar Ağaçlarının Oluşturulması:** Her alt-örneklem üzerinde bir karar ağacı oluşturulur. Bu karar ağaçları, veri setindeki özelliklerin rastgele alt kümeleri üzerinde eğitilir.

    3. **Karar Ağaçlarının Birleştirilmesi:** Oluşturulan karar ağaçları bir araya getirilir ve bir orman oluşturulur. Sınıflandırma problemleri için, her ağaç sınıf etiketi için bir oylama yapar. Regresyon problemleri için, her ağaç tahminlerini bir araya getirir ve ortalamasını alır.

    Random Forest'in ana avantajları şunlardır:

    - **Yüksek Performans:** Random Forest, birçok karar ağacının bir araya getirilmesiyle oluşturulduğu için, genellikle yüksek doğruluk ve genelleme performansı sağlar.
    - **Değişken Önem Derecelendirmesi:** Random Forest, her bir özelliğin modeldeki önemini değerlendirmek için de kullanılabilir. Bu, hangi özelliklerin modelde daha etkili olduğunu anlamak için faydalı olabilir.
    - **Veri Setindeki Gürültüye Direnç:** Random Forest, veri setindeki gürültüye ve aşırı uyuma karşı oldukça dirençlidir. Ayrıca, genellikle overfitting'e karşı daha dayanıklıdır.

    Random Forest, genellikle sınıflandırma ve regresyon problemlerinde yaygın olarak kullanılan güçlü ve esnek bir makine öğrenimi modelidir.
        """,
        
        "rbf svc": """
        RBF SVC (Radial Basis Function Support Vector Classification), destek vektör makineleri (Support Vector Machines - SVM) algoritmasının bir türüdür ve özellikle sınıflandırma problemlerinde kullanılır. SVM, bir veri kümesini sınıflandırmak için kullanılan bir öğrenme algoritmasıdır ve özellikle doğrusal olarak ayrılamayan veri setleri için etkilidir.

    RBF SVC, SVM'in bir türü olduğu için, SVM'in temel fikirleri ve prensipleri üzerine kurulmuştur. SVM, sınıflar arasındaki karar sınırlarını (decision boundaries) en iyi şekilde ayıran hiperdüzlemleri (hyperplanes) bulmaya çalışır. Ancak, RBF SVC, bu hiperdüzlemi doğrusal olmayan veri setlerinde bulmak için çekirdek fonksiyonu olarak Radial Basis Function (RBF) kullanır.

    RBF, veri noktalarının uzaklığına dayanan bir çekirdek fonksiyonudur. RBF fonksiyonu, iki veri noktası arasındaki benzerlik ölçüsünü hesaplamak için kullanılır. Bu, veri noktalarının uzayda nasıl dağıldığını dikkate alarak, veri noktalarının birbirlerine ne kadar yakın veya uzak olduklarını belirler. RBF çekirdek fonksiyonu, doğrusal olmayan karar sınırlarını tanımlamak için kullanılır.

    RBF SVC'nin avantajları şunlardır:

    1. **Esneklik:** RBF SVC, doğrusal olarak ayrılamayan veri setlerini sınıflandırmak için oldukça esnektir ve karmaşık sınıflandırma problemlerine uygundur.

    2. **Yüksek Boyutlu Veri Setleriyle Çalışma:** RBF SVC, yüksek boyutlu ve büyük ölçekli veri setleriyle iyi çalışır. Veri setinin boyutu arttıkça, RBF SVC'nin performansı genellikle düşmez.

    3. **Gürültüye Direnç:** RBF SVC, gürültülü veri setleri üzerinde iyi performans gösterir ve aşırı uyuma karşı dirençlidir.

    Ancak, RBF SVC'nin bir dezavantajı, modelin karmaşıklığı nedeniyle eğitim süresinin uzun olabilmesidir. Ayrıca, RBF SVC'nin hiperparametre ayarının doğru şekilde yapılması önemlidir; özellikle, C ve gamma gibi parametrelerin dikkatlice ayarlanması gerekebilir.
        """,
        
        "svc": """
        SVC (Support Vector Classification), destek vektör makineleri (Support Vector Machines - SVM) algoritmasının sınıflandırma problemleri için bir uygulamasıdır. SVM, özellikle doğrusal ve doğrusal olmayan sınıflandırma problemlerinde etkili olan bir makine öğrenimi algoritmasıdır.

    SVC, bir veri setini sınıflandırmak için bir karar sınırlığı (decision boundary) oluşturur. Temel amacı, sınıflar arasındaki bu karar sınırlığını en iyi şekilde ayıran bir hiperdüzlemi (hyperplane) bulmaktır. Ancak, sınıflar genellikle doğrusal olarak ayrılamaz. Bu durumda, SVC, veri noktalarını uzayda dönüştürmek için bir çekirdek fonksiyonu kullanır ve bu dönüşüm sonucu veri setinin daha yüksek boyutlu bir uzayda doğrusal olarak ayrılabilir hale gelmesini sağlar.

    SVC'nin temel özellikleri şunlardır:

    1. **Esneklik:** SVC, doğrusal ve doğrusal olmayan sınıflandırma problemlerinde etkili bir şekilde çalışabilir. Bu, farklı türdeki veri setlerine uyum sağlama esnekliği sağlar.

    2. **Küçük Veri Setleriyle Çalışma:** SVC, küçük boyutlu veri setlerinde de etkili bir şekilde çalışabilir.

    3. **Değişken Önem Derecelendirmesi:** SVC, sınıflandırma işlemi sırasında kullanılan özelliklerin önemini belirlemek için kullanılabilir.

    SVC'nin bazı dezavantajları da vardır:

    1. **Hesaplama Yoğunluğu:** SVC, büyük veri setleri üzerinde eğitilirken ve tahmin yapılırken hesaplama yoğun olabilir.

    2. **Hiperparametre Ayarı:** SVC'nin bazı hiperparametreleri vardır (örneğin, C ve çekirdek tipi), bu parametrelerin doğru şekilde ayarlanması modelin performansını etkileyebilir.

    SVC, genellikle sınıflandırma problemleri için etkili bir seçenektir ve özellikle veri setinin boyutu küçük olduğunda veya sınıflar arasında doğrusal bir ayrım yoksa tercih edilir.
        """,
        
        "xgboost": """
        XGBoost (Extreme Gradient Boosting), sınıflandırma, regresyon ve sıralama problemleri için kullanılan bir gradient boosting çerçevesidir. Gradient boosting, zayıf tahmin edicilerin (genellikle karar ağaçları) bir araya getirilerek güçlü bir tahmin edici oluşturulmasına dayanan bir makine öğrenimi tekniğidir.

    XGBoost, diğer gradient boosting kütüphanelerine kıyasla bir dizi yenilikçi teknik kullanarak hız ve performans avantajları sağlar. Bu teknikler arasında düzenlileştirme (regularization), özellik önem sıralaması, eksik değerlerin ele alınması ve özel sayısal optimizasyon algoritmaları gibi teknikler bulunur. XGBoost, bu tekniklerin yanı sıra paralel hesaplama yeteneklerini kullanarak çok büyük veri setleri üzerinde yüksek performanslı modelleme sağlar.

    XGBoost'un bazı avantajları şunlardır:

    1. **Yüksek Performans:** XGBoost, hız ve ölçeklenebilirlik açısından yüksek performans sunar. Genellikle diğer boosting yöntemlerine kıyasla daha hızlı eğitilir ve daha iyi sonuçlar verir.

    2. **Değişken Önem Derecelendirmesi:** XGBoost, modelin özelliklerin önem sıralamasını belirlemek için kullanılabilir. Bu, hangi özelliklerin modelin performansını etkilediğini anlamak için faydalıdır.

    3. **Esneklik:** XGBoost, birçok farklı makine öğrenimi probleminde kullanılabilir. Sınıflandırma, regresyon, sıralama gibi çeşitli problemleri çözebilir.

    XGBoost, özellikle Kaggle yarışmaları gibi veri bilimi yarışmalarında ve endüstriyel uygulamalarda yaygın olarak kullanılan bir makine öğrenimi aracıdır. Ayrıca, Python, R, Java, C++ gibi çeşitli programlama dillerinde kullanılabilir ve açık kaynaklı bir projedir.
        """,
        
        "yapay sinir ağları": """
        Yapay sinir ağları (YSA), insan beyninin sinir ağlarından esinlenerek oluşturulan matematiksel modeldir. Yapay sinir ağları, birçok bağlı nöron veya "hücre" adı verilen basit işlem birimlerinden oluşur. Bu nöronlar, gelen veri ve ağırlıkları kullanarak belirli bir çıktı üretirler.

    Yapay sinir ağları genellikle katmanlar halinde düzenlenir. Bir yapay sinir ağı genellikle üç ana katmandan oluşur:

    1. **Giriş Katmanı (Input Layer):** Verinin modelin içine girdiği katmandır. Giriş katmanında, her bir nöron, modele giren her bir özelliği (feature) temsil eder.

    2. **Gizli Katmanlar (Hidden Layers):** Giriş katmanının ardından bir veya daha fazla gizli katman gelir. Bu katmanlarda, veri setindeki karmaşık ilişkilerin öğrenilmesi için bir dizi işlem yapılır. Her bir gizli katmandaki nöronlar, girişlerinden gelen verileri alır, ağırlıklarla çarpar ve bir aktivasyon fonksiyonundan geçirir.

    3. **Çıkış Katmanı (Output Layer):** En son katmandır ve modelin çıktısını üretir. Sınıflandırma problemleri için genellikle çıktı katmanında softmax aktivasyon fonksiyonu kullanılırken, regresyon problemleri için doğrudan bir çıktı üretilir.

    Yapay sinir ağları, eğitim sürecinde ağırlıkların ayarlanmasıyla öğrenirler. Gerçek çıktı ile modelin tahmin ettiği çıktı arasındaki fark, bir kayıp fonksiyonu kullanılarak hesaplanır ve bu farkı minimize etmek için geriye doğru yayılım (backpropagation) algoritması kullanılarak ağırlıklar güncellenir.

    Yapay sinir ağları, geniş bir uygulama yelpazesine sahiptir. Sınıflandırma, regresyon, sinirsel dil modelleri, görüntü tanıma, ses tanıma, doğal dil işleme gibi birçok alan için başarılı bir şekilde kullanılmaktadır.
        """
        }

    user_input = st.text_input("Hakkında bilgi edinmek istediğiniz algoritma veya tekniğin adını yazınız.").lower()

    if user_input in headings_and_descriptions:
        st.write(headings_and_descriptions[user_input])
    

    if st.button("Hazırlayan"):
        st.write("Deniz ÜNLÜ")
        st.write("İletişim: denizstatistics@gmail.com")
        st.write("Linkedin: www.linkedin.com/in/deniz-ünlü-5a5036244")
        st.write("Github: https://github.com/denizzunlu")
        st.write("Kaggle: https://www.kaggle.com/denizzunlu")
    
    
    
    
elif page == "Keşifsel Veri Analizi":
    import streamlit as st
    import pandas as pd
    import numpy as np
    from contextlib import redirect_stdout
    import io
    import seaborn as sns
    import matplotlib.pyplot as plt
    import functions as functions
    from scipy.stats import norm, uniform, binom, poisson, expon, skewnorm, lognorm
    from scipy.stats import skewnorm
    import plotly.express as px
    from scipy import stats
    import statsmodels.api as sm
    from scipy.stats import shapiro, kstest
    import scipy.stats as stats
    from scipy.stats import pearsonr, spearmanr


    def perform_normality_tests(data, selected_column):
        # Shapiro-Wilk testi
        shapiro_stat, shapiro_p_value = shapiro(data[selected_column])
        # Kolmogorov-Smirnov testi
        ks_stat, ks_p_value = kstest(data[selected_column], 'norm')
        
        return shapiro_p_value, ks_p_value


    st.header("Keşifsel Veri Analizi 🔍")

    # Veri setini yükle
    allowed_formats = ["csv", "txt", "xls", "xlsx"]
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    if upload is not None:
        if "csv" in upload.name.lower():
            data = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            data = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            data = pd.read_excel(upload)

        # Tam veriyi göster
        st.subheader("Yüklenilen Veri Seti")
        st.write(data)

        st.markdown(f"*Veri Seti:* {data.shape[0]} satır, {data.shape[1]} sütun'dan oluşmaktadır.")

        # Genel Bilgileri Göster
        if st.checkbox("Veri Hakkında Genel Bilgileri Göster"):
            info_buffer = io.StringIO()
            with redirect_stdout(info_buffer):
                data.info()
            info_str = info_buffer.getvalue()
            st.text(info_str)

        # Değişken Adları
        if st.checkbox("Değişken Adlarını Göster"):
            all_columns = data.columns.to_list()
            st.write("Tüm Değişkenler:", all_columns)

        # İlk Beş Satır Butonu
        if st.checkbox("İlk Beş Satırı Göster"):
            st.write("İlk Beş Satır:")
            st.write(data.head())

        # Sondan 5 satırı göster
        if st.checkbox("Sondan 5 Satırı Göster"):
            st.write(data.tail())

        # Eksik değerleri gösterme
        if st.checkbox("Eksik Değerleri Göster"):
            st.subheader("Eksik Değerler")
            st.write(data.isnull().sum())
    

        # Betimsel İstatistikler Butonu
        if st.checkbox("Betimsel İstatistikleri Göster"):
            st.write(data.describe().T)
        

        # Dağılım Kontrolü
        if st.checkbox("Dağılım Kontrolü"):
            numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
            selected_column = st.selectbox("İncelemek istediğiniz sayısal değişkeni seçin.", numerical_columns)

            if st.button("Histogram"):
                # Histogram çizimi
                fig, ax = plt.subplots(figsize=(8, 6))
                sns.histplot(data[selected_column], kde=True, color='blue', bins=30, line_kws={'color': 'red'}, ax=ax)
                plt.title('Histogram')
                st.pyplot(fig)

            if st.button("Q-Q Plot"):
                # Q-Q plot çizimi
                fig, ax = plt.subplots(figsize=(8, 6))
                stats.probplot(data[selected_column], dist="norm", plot=ax)
                plt.title('Q-Q Plot')
                st.pyplot(fig)

            if st.button("Normal Dağılıma Uygunluk Testleri"):
                shapiro_p_value, ks_p_value = perform_normality_tests(data, selected_column)
                if shapiro_p_value >= 0.05:
                    st.write(f"Shapiro-Wilk testi sonucu P değeri {shapiro_p_value} olduğundan veri normal dağılıma uymaktadır.")
                else:
                    st.write(f"Shapiro-Wilk testi sonucu P değeri {shapiro_p_value} olduğundan veri normal dağılıma uymamaktadır.")
                
                if ks_p_value >= 0.05:
                    st.write(f"Kolmogorov-Smirnov testi sonucu P değeri {ks_p_value} olduğundan veri normal dağılıma uymaktadır.")
                else:
                    st.write(f"Kolmogorov-Smirnov testi sonucu P değeri {ks_p_value} olduğundan veri normal dağılıma uymamaktadır.")
                
                st.write("---")
    # Checkbox ile kategorik değişken grafik seçeneklerini gösterme
        show_categorical_plots = st.checkbox("Kategorik Değişkenler için Grafikler")

        if show_categorical_plots:
            # Kategorik değişkenleri seçme
            categorical_columns = data.select_dtypes(include='object').columns
            selected_categorical_column = st.selectbox("İncelemek istediğiniz kategorik değişkeni seçiniz.", categorical_columns)

            # Seçenekleri belirle
            categorical_plot_options = ["Bar Plot", "Pie Chart"]
            categorical_plot_option = st.selectbox("Grafik Türünü Seçin.", categorical_plot_options)

            if categorical_plot_option in ["Bar Plot", "Pie Chart"]:
                if categorical_plot_option == "Bar Plot":
                    fig = px.histogram(data, x=selected_categorical_column, title=f"{selected_categorical_column} Değişkeni - Bar Plot",
                                    marginal=None, hover_data=data.columns)
                
                elif categorical_plot_option == "Pie Chart":
                    fig = px.pie(data, names=selected_categorical_column, title=f"{selected_categorical_column} Değişkeni - Pie Chart")

                st.plotly_chart(fig, theme="streamlit")

            

            st.write("---")  # Değişkenler arasında ayırıcı bir çizgi ekleyelim


        # Checkbox ile grafik seçeneklerini gösterme
        show_plots = st.checkbox("Sayısal Değişkenler için Grafikler")

        if show_plots:
            #Sayısal değişkenleri seçme
            numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
            selected_column = st.selectbox("İncelemek istediğiniz değişkeni seçiniz.", numerical_columns)
            
            # Seçenekleri belirle
            options = ["Box plot", "Violin plot", "Scatter plot", "Line plot"]
            option = st.selectbox("Grafik Türünü Seçin.", options)

            if option in ["Box plot", "Violin plot", "Scatter plot", "Line plot"]:
                
                if option == "Box plot":
                    fig = px.box(data, y=selected_column, title=f'Box Plot for {selected_column}')
                    fig.update_layout(width=1000, height=600)  # Genişlik ve yüksekliği artırma
                    st.write(fig)

                elif option == "Violin plot":
                    fig = px.violin(data, y=selected_column, box=True, points="all", title=f'Violin Plot for {selected_column}')
                    fig.update_layout(width=1000, height=600)  # Genişlik ve yüksekliği artırma
                    st.write(fig)

                elif option == "Scatter plot":
                    fig = px.scatter(data, x=data.index, y=selected_column, title=f'Scatter Plot for {selected_column}')
                    fig.update_layout(width=1000, height=600)  # Genişlik ve yüksekliği artırma
                    st.write(fig)

                elif option == "Line plot":
                    fig = px.line(data, x=data.index, y=selected_column, title=f'Line Plot for {selected_column}')
                    fig.update_layout(width=1000, height=600)  # Genişlik ve yüksekliği artırma
                    st.write(fig)
                
                    
            st.write("---")  # Değişkenler arasında ayırıcı bir çizgi ekleyelim
        
        
        
            # Sayısal değişkenlerin korelasyon matrisi
            if st.checkbox("Sayısal Değişkenler Arası Korelasyon Matrisi"):
                correlation_matrix = data.select_dtypes(include=['float64', 'int64']).corr(method='pearson')
                spearman_corr_matrix = data.select_dtypes(include=['float64', 'int64']).corr(method='spearman')

                # Korelasyon matrisini göster
                st.subheader("Pearson Korelasyon Matrisi")
                st.write(correlation_matrix)

                st.subheader("Spearman Korelasyon Matrisi")
                st.write(spearman_corr_matrix)

                numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
                
                options = ["Pairplot", "Heatmap"]
                option = st.selectbox("Grafik Türünü Seçin.", options)
                
                if option == "Pairplot":
                    pair_plot_data = data[numerical_columns]
                    pair_plot = sns.pairplot(pair_plot_data)
                    plt.suptitle("Sayısal Değişkenler için PairPlot", y=1.02)
                    st.pyplot(pair_plot.fig)

                elif option == "Heatmap":
                    fig, ax = plt.subplots(figsize=(12, 8))
                    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
                    plt.title("Sayısal Değişkenlerin Pearson Korelasyon Matrisi Heatmap")
                    st.pyplot(fig)



                # Sayısal değişkenleri seç
                numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns

                # Bağımsız değişkeni seç
                independent_variable = st.selectbox("Bağımsız Değişkeni Seçiniz", numerical_columns)

                # Bağımlı değişkeni seç
                dependent_variable = st.selectbox("Bağımlı Değişkeni Seçiniz", numerical_columns)

                # Scatter plot ve lineer regresyon çizimi
                plt.figure(figsize=(10, 6))
                scatter_plot = sns.lmplot(x=independent_variable, y=dependent_variable, data=data, height=6, aspect=1.5, line_kws={'color': 'red'})
                plt.title(f"{dependent_variable} vs {independent_variable} - Scatter Plot with Regression Line")
                st.pyplot(scatter_plot.fig)

    
    
    
elif page == "Z Testi":
    import streamlit as st
    import pandas as pd
    import numpy as np
    from scipy.stats import norm
    import requests
    from io import BytesIO


    def main():
        st.title("Z Testi 📊")

        # Veri setini yükle
        allowed_formats = ["csv", "txt", "xls", "xlsx"]
        upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz", type=allowed_formats)

        if upload is not None:
            if "csv" in upload.name.lower():
                data = pd.read_csv(upload)
            elif "txt" in upload.name.lower():
                data = pd.read_csv(upload, delimiter='\t')
            elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
                data = pd.read_excel(upload)

            st.write("Veri Örneği:")
            st.write(data)

            # Z-testi için gereken bilgilerin girişi
            st.subheader("Z-Testi Parametreleri")
            if not data.empty:
                mu_default = float(data.mean().values[0])
                sigma_default = float(data.std().values[0])
                sample_mean_min = float(data.min().values[0])
                sample_mean_max = float(data.max().values[0])
                n_default = min(max(30, len(data)), 100)
            else:
                mu_default = 0.0
                sigma_default = 1.0
                sample_mean_min = None
                sample_mean_max = None
                n_default = 30
            
            mu = st.number_input("Popülasyon Ortalaması (μ)", value=mu_default)
            sigma = st.number_input("Popülasyon Standart Sapması (σ)", value=sigma_default)
            sample_mean = st.number_input("Örneklem Ortalaması", value=mu_default)
            n = st.number_input("Örneklem Büyüklüğü (n)", value=n_default)

            # Z-testi istatistiğinin hesaplanması
            z_stat = (sample_mean - mu) / (sigma / np.sqrt(n))

            # P-değeri hesaplanması
            p_value = 2 * (1 - norm.cdf(np.abs(z_stat)))

            # Sonuçların gösterilmesi
            st.subheader("Z-Testi Sonuçları")
            st.write("Z-istatistiği:", z_stat)
            st.write("P-değeri:", p_value)

    if __name__ == "__main__":
        main()

    


    
elif page == "T Testi":
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    from scipy import stats
    import numpy as np




    def perform_normality_tests_independent(data, dependent_variable, independent_variable):
        group_names = data[independent_variable].unique()
        shapiro_p_values = {}
        ks_p_values = {}
        for group in group_names:
            group_data = data[data[independent_variable] == group][dependent_variable]
            _, shapiro_p_value = stats.shapiro(group_data)
            _, ks_p_value = stats.kstest(group_data, 'norm')
            shapiro_p_values[group] = shapiro_p_value
            ks_p_values[group] = ks_p_value
        return shapiro_p_values, ks_p_values


    def perform_normality_tests(data, independent_variables):
        shapiro_p_values = {}
        ks_p_values = {}
        for variable in independent_variables:
            _, shapiro_p_value = stats.shapiro(data[variable])
            _, ks_p_value = stats.kstest(data[variable], 'norm')
            shapiro_p_values[variable] = shapiro_p_value
            ks_p_values[variable] = ks_p_value
        return shapiro_p_values, ks_p_values

    def perform_one_sample_t_test(data, column, null_hypothesis_value):
        t_statistic, p_value = stats.ttest_1samp(data[column], null_hypothesis_value)
        return t_statistic, p_value

    def perform_independent_t_test(data, test_variables, grouping_variable, group1, group2, confidence_level):
        group1_data = data[data[grouping_variable] == group1][test_variables]
        group2_data = data[data[grouping_variable] == group2][test_variables]
        
        statistic, levene_p_value = stats.levene(group1_data.squeeze(), group2_data.squeeze())
        
        alpha = 1 - confidence_level / 100
        if levene_p_value > alpha:
            t_statistic, p_value = stats.ttest_ind(group1_data.squeeze(), group2_data.squeeze(), equal_var=True)
            var_assumption = "Homojen"
        else:
            t_statistic, p_value = stats.ttest_ind(group1_data.squeeze(), group2_data.squeeze(), equal_var=False)
            var_assumption = "Homojen Değil"
        return t_statistic, p_value, var_assumption, levene_p_value

    def perform_dependent_t_test(data, variable1, variable2, confidence_level):
        t_statistic, p_value = stats.ttest_rel(data[variable1], data[variable2])
        return t_statistic, p_value

    def descriptive_statistics(data):
        return data.describe()

    st.title("T Testi 📊")
    st.subheader("Tek Örneklem T Testi")
    st.write("Tek örneklem t-testi, bir popülasyonun ortalaması hakkında bir tahmin yapmak veya karşılaştırmak için kullanılır.")

    st.subheader("İki Örneklem Bağımsız T Testi")
    st.write(" İki örneklem bağımsız t-testi, iki farklı grup arasındaki ortalama farkını karşılaştırmak için kullanılır. Bu gruplar birbirinden bağımsızdır, yani bir gruptaki gözlemler diğer gruptaki gözlemlerden bağımsızdır.")

    st.subheader("İki Örneklem Bağımlı T Testi")
    st.write(" İki örneklem bağımlı t-testi, aynı bireylerin iki farklı zaman noktasında alınan ölçümleri arasındaki ortalama farkı karşılaştırmak için kullanılır. Bu ölçümler arasındaki ilişki dolayısıyla bağımlılık vardır.")




    # Veri setini yükle
    allowed_formats = ["csv", "txt", "xls", "xlsx"]
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz", type=allowed_formats)

    if upload is not None:
        if "csv" in upload.name.lower():
            data = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            data = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            data = pd.read_excel(upload)

        if data is not None:  # Veri yüklenirse devam et
            # Verinin önizlemesini göster
            st.subheader("Yüklenilen Veri Seti")
            st.write(data)

            # Betimsel İstatistikler
            st.subheader("Betimsel İstatistikler")
            st.write(data.describe())

            
            # Hipotez testi seçimi
            test_type = st.selectbox('Hipotez Testi Türü Seçin:', ['-', 'Tek Örneklem T Testi', 'Bağımsız Örneklem T Testi', 'Bağımlı Örneklem T Testi'])
            
            if test_type != '-':
                # Güvenilirlik düzeyini al
                confidence_level = st.slider("Güvenilirlik Düzeyini Seçin:", min_value=1, max_value=99, value=95, step=1)

                if test_type == 'Tek Örneklem T Testi':
                    st.header('Tek Örneklem T Testi')
                    sample_column = st.selectbox('Örnek veri sütunu seçin:', data.columns)
                    null_hypothesis_value = st.number_input('Test değerini girin:')
                    t_statistic, p_value = perform_one_sample_t_test(data, sample_column, null_hypothesis_value)
                    st.write('T İstatistiği:', t_statistic)
                    st.write('P Değeri(Significance):', p_value)
                    alpha = 1 - confidence_level / 100
                    if p_value < alpha:
                        st.write("H0 reddedilir.")
                    else:
                        st.write("H0 kabul edilir.")


                
                if test_type == 'Bağımsız Örneklem T Testi':
                    st.subheader('Bağımsız Örneklem T Testi')
                    
                    # Test değişkenlerini seç
                    test_variables = st.multiselect('Test Variable(s) seçin:', options=data.columns)
                    grouping_variable = st.selectbox('Grouping Variable seçin:', options=data.select_dtypes(include=['object']).columns)

                    # Grupları otomatik olarak belirle
                    group_names = data[grouping_variable].unique().tolist()
                    group1 = group_names[0]
                    group2 = group_names[1]

                    # Normal dağılıma uygunluk testleri yap
                    shapiro_p_values, ks_p_values = perform_normality_tests_independent(data, test_variables, grouping_variable)

                    # Sonuçları göster
                    st.subheader("Normal Dağılıma Uygunluk Testi")
                    st.write("Bağımlı Değişken:", test_variables[0])
                    st.write("Bağımlı Değişken Bakımından İncelenen Değişken:", grouping_variable)
                    st.write("---")
                    st.write("Shapiro-Wilk Testi P Değerleri:")
                    for group, p_value in shapiro_p_values.items():
                        st.write(f"{group}: {np.format_float_positional(p_value, precision=4)}")
                        
                    st.write("---")
                    
                    st.write("Kolmogorov-Smirnov Testi P Değerleri:")
                    for group, p_value in ks_p_values.items():
                        st.write(f"{group}: {float(p_value):.4f}")
                    st.write("---")
                    st.write("Shapiro-Wilk testi, örneklem büyüklüğü yaklaşık 50 veya daha az olduğunda daha güvenilir sonuçlar verir. ")
                    st.write("Kolmogorov-Smirnov testi, örneklem büyüklüğü 50'den büyükse daha güvenilir sonuçlar verir.") 
                    st.write("---")
                    # Bağımsız Örnekler T Testi
                    t_statistic, p_value, var_assumption, levene_p_value = perform_independent_t_test(data, test_variables, grouping_variable, group1, group2, confidence_level)
                    if levene_p_value > 0.05:
                        st.write('Levene testi p değeri:', np.format_float_positional(levene_p_value, precision=4), 'olduğundan varyanslar homojen.')
                        st.write("---")
                        st.write('Bağımsız Örnekler T Testi İstatistiği:', np.format_float_positional(t_statistic, precision=4))
                        st.write('P Değeri:', np.format_float_positional(p_value, precision=4))
                    else:
                        st.write('Levene Testi p değeri:', np.format_float_positional(levene_p_value, precision=4), 'olduğundan varyanslar homojen değil.')
                        st.write('Welch\'s T Testi İstatistiği ve P Değeri:', np.format_float_positional(t_statistic, precision=4), np.format_float_positional(p_value, precision=4))
                    
                    st.write("---")
                    
                    # Grafiksel sunumlar
                    fig = px.box(data, x=grouping_variable, y=test_variables[0], title='Gruplar Arasındaki Dağılım')
                    fig.update_layout(width=1000, height=600)  # Genişlik ve yüksekliği artırma
                    st.plotly_chart(fig)




                elif test_type == 'Bağımlı Örneklem T Testi':
                    st.subheader('Bağımlı Örneklem T Testi')
                    variable1 = st.selectbox('Değişken 1 seçin:', options=data.columns)
                    variable2 = st.selectbox('Değişken 2 seçin:', options=data.columns)

                    # Kolmogorov-Smirnov ve Shapiro-Wilk testlerini gerçekleştir
                    independent_variables = [variable1, variable2]
                    shapiro_p_values, ks_p_values = perform_normality_tests(data, independent_variables)

                    st.write("İncelenen Değişkenler:", independent_variables)
                    st.write("Shapiro-Wilk Testi P Değerleri:")
                    for variable, p_value in shapiro_p_values.items():
                        st.write(f"{variable}: {p_value:.4f}")
                    st.write("---")
                    st.write("Kolmogorov-Smirnov Testi P Değerleri:")
                    for variable, p_value in ks_p_values.items():
                        st.write(f"{variable}: {p_value:.4f}")
                    st.write("---")
                    st.write("Shapiro-Wilk testi, örneklem büyüklüğü yaklaşık 50 veya daha az olduğunda daha güvenilir sonuçlar verir. ")
                    st.write("Kolmogorov-Smirnov testi, örneklem büyüklüğü 50'den büyükse daha güvenilir sonuçlar verir.")
                    st.write("---")
                    st.write(data.describe())
                    st.write("---")
                    # Bağımlı Örneklem T Testi
                    t_statistic, p_value = perform_dependent_t_test(data, variable1, variable2, confidence_level)
                    st.write('T İstatistiği:', t_statistic)
                    st.write('P Değeri(Significance):', p_value)
                    alpha = 1 - confidence_level / 100
                    if p_value < alpha:
                        st.write("H0 reddedilir.")
                    else:
                        st.write("H0 kabul edilir.")

    
    

    
elif page == "Basit Doğrusal Regresyon":
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    import statsmodels.formula.api as smf

    # Streamlit başlığı
    st.title("Basit Doğrusal Regresyon 📈")

    # Veri yükleme işlemi
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, mean_absolute_error
    import statsmodels.formula.api as smf

    # Veri yükleme işlemi
    allowed_formats = ["csv", "txt", "xls", "xlsx"]
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        st.write(df)
        st.write("---")
        # Bağımlı ve bağımsız değişken seçimi
        st.subheader("Bağımlı ve Bağımsız Değişken Seçimi")
        X_col = st.selectbox("Bağımsız Değişkeni Seçin", options=df.columns)
        y_col = st.selectbox("Bağımlı Değişkeni Seçin", options=df.columns)

        # Eğitim-test veri seti bölme oranı
        test_size = st.slider("Test Veri Seti Boyutu (%)", 0.1, 0.5, 0.2, 0.05)

        # Random state değerini kullanıcıdan al
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("---")
        # Model eğitimi
        X = df[[X_col]].values
        y = df[y_col].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        lr = LinearRegression()
        lr.fit(X_train, y_train)

        # Tahminlerin hesaplanması
        y_pred = lr.predict(X_test)

        # Model performansı ölçümleri (MSE, RMSE, MAE)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_test, y_pred)
        
        # Model performansı ölçümlerinin görüntülenmesi
        st.subheader("Model Performansı")
        st.write(f"Mean Squared Error (MSE): {mse}")
        st.write(f"Root Mean Squared Error (RMSE): {rmse}")
        st.write(f"Mean Absolute Error (MAE): {mae}")
        st.write("---")

        # Model performansı
        reg_summary = smf.ols(f"{y_col} ~ {X_col}", df).fit()
        st.write(reg_summary.summary())
        st.write("---")
        # Model parametrelerinin denklemi
        st.subheader("Tahmin Edilen Modelin Denklemi")
        st.latex(rf"Y = {lr.intercept_} + {lr.coef_[0]} \times X")

        # Model parametreleri
        st.subheader("Tahmin Edilen Modelin Parametreleri")
        st.write(f"Sabit Katsayı (B0): {lr.intercept_}")
        st.write(f"Eğim Katsayısı (B1): {lr.coef_[0]}")
        st.write("---")
        
        # Tahmin
        st.subheader("Tahmin")
        input_value = st.number_input("Tahmin etmek istediğiniz değeri girin:")
        prediction = lr.predict([[input_value]])
        st.write("Tahmini Değer:", prediction)

            
       
       
    
elif page == "Çoklu Doğrusal Regresyon":
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    import statsmodels.formula.api as smf

    # Streamlit başlığı
    st.title("Çoklu Doğrusal Regresyon 📊📈")

    # Veri yükleme işlemi
    allowed_formats = ["csv", "txt", "xls", "xlsx"]
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        st.write(df)
        st.write("---")
        # Bağımlı ve bağımsız değişken seçimi
        st.subheader("Bağımlı ve Bağımsız Değişken Seçimi")
        X_cols = st.multiselect("Bağımsız Değişkenleri Seçin", options=df.columns)
        y_col = st.selectbox("Bağımlı Değişkeni Seçin", options=df.columns)

        # Eğitim-test veri seti bölme oranı
        test_size = st.slider("Test Veri Seti Boyutu (%)", 0.1, 0.5, 0.2, 0.05)

        # Random state değerini kullanıcıdan al
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("---")
        # Model eğitimi
        X = df[X_cols].values
        y = df[y_col].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        lr = LinearRegression()
        lr.fit(X_train, y_train)

        # Model performansı (CV öncesi)
        st.subheader("Model Performansı (CV Öncesi)")
        train_rmse = np.sqrt(mean_squared_error(y_train, lr.predict(X_train)))
        test_rmse = np.sqrt(mean_squared_error(y_test, lr.predict(X_test)))
        train_r2_score = lr.score(X_train, y_train)
        st.write("Eğitim Seti RMSE:", train_rmse)
        st.write("Test Seti RMSE:", test_rmse)
        st.write("Eğitim Seti R^2 Score:", train_r2_score)
        st.write("---")

        # Çapraz doğrulama sonrası skorları hesapla
        cv_r2_scores = cross_val_score(lr, X_train, y_train, cv=10, scoring='r2')
        cv_rmse_train_scores = np.sqrt(-cross_val_score(lr, X_train, y_train, cv=10, scoring='neg_mean_squared_error'))
        cv_rmse_test_scores = np.sqrt(-cross_val_score(lr, X_test, y_test, cv=10, scoring='neg_mean_squared_error'))

        cv_r2_score = cv_r2_scores.mean()
        cv_rmse_train = cv_rmse_train_scores.mean()
        cv_rmse_test = cv_rmse_test_scores.mean()

        # CV öncesi ve sonrası sonuçları karşılaştırma
        st.subheader("CV Öncesi ve Sonrası Karşılaştırma")

        # Tabloyu oluşturmak için verileri birleştirme
        comparison_data = {
            "": ["Eğitim Öncesi CV", "Eğitim Sonrası CV"],
            "RMSE (Eğitim Seti)": [train_rmse, cv_rmse_train],
            "RMSE (Test Seti)": [test_rmse, cv_rmse_test],
            "R^2 Score (Eğitim Seti)": [train_r2_score, cv_r2_score]
        }

        # DataFrame oluşturma
        comparison_df = pd.DataFrame(comparison_data)

        # Sonuçları tablo şeklinde gösterme
        st.write(comparison_df)

        # Model performansı
        st.subheader("Model Performansı")
        reg_summary = smf.ols(f"{y_col} ~ {' + '.join(X_cols)}", df).fit()
        st.write(reg_summary.summary())
        st.write("---")
        # Model parametrelerinin denklemi
        st.subheader("Tahmin Edilen Modelin Denklemi")
        equation = f"{lr.intercept_}"
        for i, col in enumerate(X_cols):
            equation += f" + ({lr.coef_[i]} * {col})"
        st.latex(rf"Y = {equation}")

        # Model parametreleri
        st.subheader("Tahmin Edilen Modelin Parametreleri")
        st.write(f"Sabit Katsayı (B0): {lr.intercept_}")
        for i, col in enumerate(X_cols):
            st.write(f"Eğim Katsayısı ({col}): {lr.coef_[i]}")
        st.write("---")
        # Tahmin
        st.subheader("Tahmin")
        input_values = []
        for col in X_cols:
            input_val = st.number_input(f"{col} değerini girin:")
            input_values.append(input_val)
        prediction = lr.predict([input_values])
        st.write("Tahmini Değer:", prediction[0])

    
    
    
elif page == "Fisher's Exact Testi":
    import streamlit as st
    import pandas as pd
    from scipy.stats import fisher_exact

    def main():
        st.title("Fisher's Exact 📝")

        allowed_formats = ["csv", "txt", "xls", "xlsx"]
        upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

        if upload is not None:
            if "csv" in upload.name.lower():
                data = pd.read_csv(upload)
            elif "txt" in upload.name.lower():
                data = pd.read_csv(upload, delimiter='\t')
            elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
                data = pd.read_excel(upload)


            st.write("Yüklenen Veri Seti:")
            st.write(data)

            # Kullanıcıdan kategorik değişken seçimi al
            st.subheader("Fisher's Exact Testi için Değişkenlerin Seçimi")
            variable1 = st.selectbox("Lütfen birinci kategorik değişkeni seçin:", data.columns)
            variable2 = st.selectbox("Lütfen ikinci kategorik değişkeni seçin:", data.columns)

            # Fisher's Exact testinin yapılması için uygun tabloyu oluştur
            contingency_table = pd.crosstab(data[variable1], data[variable2])

            if contingency_table.shape == (2, 2):
                # Fisher's Exact testi sonuçlarını göster
                st.subheader("Fisher's Exact Testi Sonuçları")
                oddsratio, p_value = fisher_exact(contingency_table)
                st.write("Odds Ratio:", oddsratio)
                st.write("P-değeri:", p_value)

                # Sonuçların yorumlanması
                if p_value < 0.05:
                    st.write("P-değeri 0.05 anlamlılık düzeyinden küçük olduğu için, değişkenler arasında istatistiksel olarak anlamlı bir ilişki vardır.")
                else:
                    st.write("P-değeri 0.05 anlamlılık düzeyinden büyük olduğu için, değişkenler arasında istatistiksel olarak anlamlı bir ilişki yoktur.")
            else:
                st.write("Fisher's Exact Testi için uygun tablo oluşturulamadı. Lütfen verilerinizi kontrol edin ve tekrar deneyin.")

    if __name__ == "__main__":
        main()

    
    
    
elif page == "Ki-Kare Testi":
    import streamlit as st
    import pandas as pd
    from scipy.stats import chi2_contingency

    def main():
        st.title("Ki-Kare Testi 📊")

        # Veri setini yükle
        allowed_formats = ["csv", "txt", "xls", "xlsx"]
        upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

        if upload is not None:
            if "csv" in upload.name.lower():
                data = pd.read_csv(upload)
            elif "txt" in upload.name.lower():
                data = pd.read_csv(upload, delimiter='\t')
            elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
                data = pd.read_excel(upload)

            st.write("Veri Seti")
            st.write(data)
        
            
            # Ki-kare testi için kategorik sütunların seçimi
            st.subheader("Ki-kare Testi için Kategorik Sütunlar")
            categorical_columns = st.multiselect("Lütfen kategorik sütunları seçin:", data.columns)

            if len(categorical_columns) > 1:
                # Frekans tablosunu oluştur
                contingency_table = pd.crosstab(data[categorical_columns[0]], data[categorical_columns[1]])

                # Ki-kare testinin yapılması
                st.subheader("Ki-kare Testi Sonuçları")
                chi2_result = chi2_contingency(contingency_table)
                st.write("Ki-kare İstatistiği:", chi2_result[0])
                st.write("P-değeri:", chi2_result[1])
            else:
                st.write("Lütfen en az 2 kategorik sütun seçin.")

    if __name__ == "__main__":
        main()

    
    
    
elif page == "Kruskal-Wallis Testi":
    import streamlit as st
    import pandas as pd
    from scipy.stats import kruskal

    def main():
        st.title("Kruskal Wallis Testi 📊")

        # Veri setini yükle
        allowed_formats = ["csv", "txt", "xls", "xlsx"]
        upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

        if upload is not None:
            if "csv" in upload.name.lower():
                data = pd.read_csv(upload)
            elif "txt" in upload.name.lower():
                data = pd.read_csv(upload, delimiter='\t')
            elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
                data = pd.read_excel(upload)

            st.write("Veri Örneği:")
            st.write(data)

            # Kruskal-Wallis testi için grup seçimi
            st.subheader("Kruskal-Wallis Testi için Gruplar")
            groups = st.multiselect("Lütfen grupları seçin:", data.columns)

            if len(groups) >= 3:
                # Kruskal-Wallis testinin yapılması
                st.subheader("Kruskal-Wallis Testi Sonuçları")
                stat, p_value = kruskal(*[data[group] for group in groups])
                st.write("Test İstatistiği:", stat)
                st.write("P-değeri:", p_value)

                # Sonuçların yorumlanması
                if p_value < 0.05:
                    st.write("P-değeri 0.05 anlamlılık düzeyinden küçük olduğu için, gruplar arasında istatistiksel olarak anlamlı bir fark vardır.")
                else:
                    st.write("P-değeri 0.05 anlamlılık düzeyinden büyük olduğu için, gruplar arasında istatistiksel olarak anlamlı bir fark yoktur.")
            else:
                st.write("Lütfen en az üç grup seçin.")

    if __name__ == "__main__":
        main()

    
    
elif page == "Wilcoxon İşaretli Sıralar Testi":
    import streamlit as st
    import pandas as pd
    from scipy.stats import wilcoxon

    def main():
        st.title("Wilcoxon İşaretli Sıralar Testi 📈")

        # Veri setini yükle
        allowed_formats = ["csv", "txt", "xls", "xlsx"]
        upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

        if upload is not None:
            if "csv" in upload.name.lower():
                data = pd.read_csv(upload)
            elif "txt" in upload.name.lower():
                data = pd.read_csv(upload, delimiter='\t')
            elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
                data = pd.read_excel(upload)

            st.write("Veri Örneği:")
            st.write(data.head())

            # Wilcoxon testi için grup seçimi
            st.subheader("Wilcoxon Testi için Gruplar")
            group1 = st.selectbox("Lütfen birinci grubu seçin:", data.columns)
            group2 = st.selectbox("Lütfen ikinci grubu seçin:", data.columns)

            # Wilcoxon testinin yapılması
            st.subheader("Wilcoxon Testi Sonuçları")
            stat, p_value = wilcoxon(data[group1], data[group2])
            st.write("Test İstatistiği:", stat)
            st.write("P-değeri:", p_value)

            # Sonuçların yorumlanması
            if p_value < 0.05:
                st.write("P-değeri 0.05 anlamlılık düzeyinden küçük olduğu için, gruplar arasında istatistiksel olarak anlamlı bir fark vardır.")
            else:
                st.write("P-değeri 0.05 anlamlılık düzeyinden büyük olduğu için, gruplar arasında istatistiksel olarak anlamlı bir fark yoktur.")

    if __name__ == "__main__":
        main()

    
    
elif page == "CART (Classification and Regression Trees)":
    
    st.title("CART (Sınıflandırma ve Regresyon Ağaçları) 📊🔍")
    import streamlit as st
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, mean_squared_error, mean_absolute_error
    from sklearn.metrics import confusion_matrix
    import matplotlib.pyplot as plt
    from sklearn.model_selection import GridSearchCV

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        # Yüklenen dosyanın formatına göre veriyi okuma
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)
        
        
        
        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            # Bağımsız ve bağımlı değişkenleri seçme
            st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
            X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
            y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
            X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
            y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

            # Bağımsız ve bağımlı değişkenleri ayırma
            X = df[X_selected]
            y = df[y_selected]

            # Test verisi yüzdesi ve random state değeri girişi
            test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
            random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
            st.write("----")
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # CART sınıflandırma modeli oluşturma ve eğitme
            cart_model = DecisionTreeClassifier().fit(X_train, y_train)
            y_pred = cart_model.predict(X_test)

            # AUC-ROC
            st.subheader("ROC Eğrisi ve AUC Değeri")
            cart_roc_auc = roc_auc_score(y_test, cart_model.predict_proba(X_test)[:, 1])
            fpr, tpr, thresholds = roc_curve(y_test, cart_model.predict_proba(X_test)[:,1])

            fig, ax = plt.subplots()
            ax.plot(fpr, tpr, label='AUC (area = %0.2f)' % cart_roc_auc)
            ax.plot([0, 1], [0, 1],'r--')
            ax.set_xlim([0.0, 1.0])
            ax.set_ylim([0.0, 1.05])
            ax.set_xlabel('False Positive Oranı')
            ax.set_ylabel('True Positive Oranı')
            ax.set_title('ROC')
            st.pyplot(fig)

            st.write("AUC Değeri:", cart_roc_auc)

            # Doğruluk (Accuracy)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy):", accuracy)

            # Hassasiyet (Precision)
            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision):", precision)

            # Geri Çağırma (Recall)
            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall):", recall)

            # F1-Skor
            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor:", f1)

            # Confusion Matrix
            st.subheader("Karmaşıklık Matrisi:")
            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix, 
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.write(conf_matrix_df)


        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Bağımsız ve bağımlı değişkenleri seçme
            st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
            X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  
            y_options = df.select_dtypes(include=['number', 'float']).columns.tolist()  
            X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
            y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

            # Bağımsız ve bağımlı değişkenleri ayırma
            X = df[X_selected]
            y = df[y_selected]

            # Veri kümesini eğitim ve test kümelerine ayırma
            test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
            random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
            st.write("----")

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # CART regresyon modeli oluşturma
            cart_model = DecisionTreeRegressor()
            cart_model.fit(X_train, y_train)

            y_pred = cart_model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Model ortalama kare hatası (MSE):", mse)
            st.write("Model ortalama mutlak hatası (MAE):", mae)
            st.write("Model kök ortalama kare hatası (RMSE):", rmse)

            # Model hiperparametre optimizasyonu
            cart_params = {
                'max_depth': [3, 5, 7],
                'min_samples_split': [2, 5, 10]
            }
            cart = DecisionTreeRegressor()
            cart_cv_model = GridSearchCV(cart, cart_params, cv=3, n_jobs=-1, verbose=2)
            cart_cv_model.fit(X_train, y_train)
            best_params = cart_cv_model.best_params_
            st.write("En iyi parametreler:", best_params)

            # Optimize edilmiş modeli kullanma
            cart_tuned = DecisionTreeRegressor(**best_params)
            cart_tuned.fit(X_train, y_train)
            y_pred_tuned = cart_tuned.predict(X_test)
            mse_tuned = mean_squared_error(y_test, y_pred_tuned)
            mae_tuned = mean_absolute_error(y_test, y_pred_tuned)
            rmse_tuned = mean_squared_error(y_test, y_pred_tuned, squared=False)
            st.write("Optimize edilmiş model ortalama kare hatası (MSE):", mse_tuned)
            st.write("Optimize edilmiş model ortalama mutlak hatası (MAE):", mae_tuned)
            st.write("Optimize edilmiş model kök ortalama kare hatası (RMSE):", rmse_tuned)
    
    
    
elif page == "CatBoost":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_error,precision_score,recall_score, f1_score, roc_auc_score, confusion_matrix,roc_curve
    from catboost import CatBoostClassifier, CatBoostRegressor
    import matplotlib.pyplot as plt
    
    
    st.title("Catboost 🔢")
    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")
        
        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # CatBoost sınıflandırma modeli oluşturma ve eğitme
            cat_model = CatBoostClassifier().fit(X_train, y_train)
            y_pred = cat_model.predict(X_test)


            # AUC-ROC
            st.subheader("ROC Eğrisi ve AUC Değeri")
            cat_roc_auc = roc_auc_score(y_test, cat_model.predict_proba(X_test)[:, 1])
            fpr, tpr, thresholds = roc_curve(y_test, cat_model.predict_proba(X_test)[:,1])

            fig, ax = plt.subplots()
            ax.plot(fpr, tpr, label='AUC (area = %0.2f)' % cat_roc_auc)
            ax.plot([0, 1], [0, 1],'r--')
            ax.set_xlim([0.0, 1.0])
            ax.set_ylim([0.0, 1.05])
            ax.set_xlabel('False Positive Oranı')
            ax.set_ylabel('True Positive Oranı')
            ax.set_title('ROC')
            st.pyplot(fig)

            st.write("AUC Değeri:", cat_roc_auc)

            # Doğruluk (Accuracy)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy):", accuracy)

            # Hassasiyet (Precision)
            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision):", precision)

            # Geri Çağırma (Recall)
            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall):", recall)

            # F1-Skor
            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor:", f1)
            
            
            
            # Confusion Matrix
            st.subheader("Karmaşıklık Matrisi:")
            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix, 
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.write(conf_matrix_df)

        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # CatBoost regresyon modeli oluşturma
            cat_model = CatBoostRegressor().fit(X_train, y_train)
            y_pred = cat_model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Model ortalama kare hatası (MSE):", mse)
            st.write("Model ortalama mutlak hatası (MAE):", mae)
            st.write("Model kök ortalama kare hatası (RMSE):", rmse)

            # Model hiperparametre optimizasyonu
            cat_params = {
                'iterations': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'depth': [3, 5, 7]
            }
            cat = CatBoostRegressor()
            cat_cv_model = GridSearchCV(cat, cat_params, cv=5, n_jobs=-1, verbose=2)
            cat_cv_model.fit(X_train, y_train)
            best_params = cat_cv_model.best_params_
            st.write("En iyi parametreler:", best_params)

            # Optimize edilmiş modeli kullanma
            cat_tuned = CatBoostRegressor(**best_params)
            cat_tuned.fit(X_train, y_train)
            y_pred_tuned = cat_tuned.predict(X_test)
            mse_tuned = mean_squared_error(y_test, y_pred_tuned)
            mae_tuned = mean_absolute_error(y_test, y_pred_tuned)
            rmse_tuned = mean_squared_error(y_test, y_pred_tuned, squared=False)
            st.write("Optimize edilmiş model ortalama kare hatası (MSE):", mse_tuned)
            st.write("Optimize edilmiş model ortalama mutlak hatası (MAE):", mae_tuned)
            st.write("Optimize edilmiş model kök ortalama kare hatası (RMSE):", rmse_tuned)


    
elif page == "Gaussian Naive Bayes":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score,roc_curve, roc_auc_score
    from sklearn.model_selection import cross_val_score
    import matplotlib.pyplot as plt
    
    # Sayfa başlığı
    st.title("Gaussian Naive Bayes 🔢")

    # Desteklenen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyin", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        # Yüklenen dosyanın formatına göre veriyi okuma
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)
        
        
        st.write("Yüklenen Veri Seti:")
        st.write(df.head())

        # Bağımsız ve bağımlı değişkenleri seçme bölümü
        st.header("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_cols = st.multiselect("Lütfen bağımsız değişkenleri seçin", df.columns)
        y_col = st.selectbox("Lütfen bağımlı değişkeni seçin", df.columns)
        st.write("----")
        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_cols]
        y = df[y_col]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")
        # Veri kümesini eğitim ve test kümelerine ayırma
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # Gaussian Naive Bayes modelini oluşturma ve eğitme
        st.header("Gaussian Naive Bayes Modeli Oluşturma")
        nb = GaussianNB()
        nb_model = nb.fit(X_train, y_train)

        # Modeli değerlendirme
        st.header("Model Değerlendirme")
        y_pred = nb_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write("Doğruluk:", accuracy)
        st.write("----")
        # Confusion Matrix
        st.subheader("Karmaşıklık Matrisi:")
        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_matrix_df = pd.DataFrame(conf_matrix, 
                                    columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                    index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
        st.write(conf_matrix_df)
        st.write("----")
        # Sınıflandırma Raporu
        st.subheader("Sınıflandırma Raporu")
        class_report = classification_report(y_test, y_pred, output_dict=True)
        class_report_df = pd.DataFrame(class_report).transpose()
        st.write(class_report_df)
        # AUC-ROC
        st.subheader("ROC Eğrisi ve AUC Değeri")
        cat_roc_auc = roc_auc_score(y_test, nb_model.predict_proba(X_test)[:, 1])
        fpr, tpr, thresholds = roc_curve(y_test, nb_model.predict_proba(X_test)[:,1])

        fig, ax = plt.subplots()
        ax.plot(fpr, tpr, label='AUC (area = %0.2f)' % cat_roc_auc)
        ax.plot([0, 1], [0, 1],'r--')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Oranı')
        ax.set_ylabel('True Positive Oranı')
        ax.set_title('ROC')
        st.pyplot(fig)

        st.write("AUC Değeri:", cat_roc_auc)

        st.write("----")

        # Cross validation
        st.header("Çapraz Doğrulama")
        cv_scores = cross_val_score(nb_model, X, y, cv=10).mean()
        st.write("Çapraz Doğrulama Skoru:", cv_scores)

    
    
elif page == "Gradient Boosting Machines":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    st.title("Gradient Boosting Machine 🔢")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")
        
        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # GBM sınıflandırma modeli oluşturma
            gbm = GradientBoostingClassifier()

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(gbm, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            gbm_model = GradientBoostingClassifier(**best_params)
            gbm_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme
            y_pred = gbm_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy):", accuracy)

            # Diğer performans metriklerini hesaplama ve görselleştirme
            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor:", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru:", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix, 
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi:")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi')
            plt.legend(loc="lower right")
            st.pyplot(plt)

        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # GBM regresyon modeli oluşturma
            gbm = GradientBoostingRegressor()
            gbm.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme
            y_pred = gbm.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu öncesi modelin kök ortalama kare hatası (RMSE):", rmse)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(gbm, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            gbm_model = GradientBoostingRegressor(**best_params)
            gbm_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme
            y_pred = gbm_model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu sonrası modelin kök ortalama kare hatası (RMSE):", rmse)


    
    
elif page == "K-En Yakın Komşu (KNN)":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    st.title("Gradient Boosting Machine 🔢")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # GBM sınıflandırma modeli oluşturma
            gbm = GradientBoostingClassifier()
            gbm.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = gbm.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre öncesi):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre öncesi):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre öncesi):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre öncesi):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre öncesi):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre öncesi):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre öncesi)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre öncesi)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(gbm, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            gbm_model = GradientBoostingClassifier(**best_params)
            gbm_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = gbm_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre sonrası):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre sonrası):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre sonrası):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre sonrası):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre sonrası):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre sonrası):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre sonrası)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre sonrası)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # GBM regresyon modeli oluşturma
            gbm = GradientBoostingRegressor()
            gbm.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = gbm.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu öncesi modelin kök ortalama kare hatası (RMSE):", rmse)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(gbm, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            gbm_model = GradientBoostingRegressor(**best_params)
            gbm_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = gbm_model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu sonrası modelin kök ortalama kare hatası (RMSE):", rmse)

        
    
elif page == "LightGBM":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from lightgbm import LGBMClassifier, LGBMRegressor
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    st.title("LightGBM 🔢")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # LightGBM sınıflandırma modeli oluşturma
            lgbm = LGBMClassifier()
            lgbm.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = lgbm.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre öncesi):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre öncesi):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre öncesi):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre öncesi):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre öncesi):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre öncesi):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre öncesi)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre öncesi)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(lgbm, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            lgbm_model = LGBMClassifier(**best_params)
            lgbm_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = lgbm_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre sonrası):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre sonrası):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre sonrası):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre sonrası):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre sonrası):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre sonrası):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre sonrası)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre sonrası)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # LightGBM regresyon modeli oluşturma
            lgbm = LGBMRegressor()
            lgbm.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = lgbm.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu öncesi modelin kök ortalama kare hatası (RMSE):", rmse)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(lgbm, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            lgbm_model = LGBMRegressor(**best_params)
            lgbm_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = lgbm_model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu sonrası modelin kök ortalama kare hatası (RMSE):", rmse)

    
    
elif page == "Lojistik Regresyon":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as plt

    st.title("Lojistik Regresyon 🔢")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma işlemleri
        if st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon")) == "Sınıflandırma":
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # Lojistik Regresyon modeli oluşturma
            logreg = LogisticRegression()
            logreg.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = logreg.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre öncesi):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre öncesi):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre öncesi):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre öncesi):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre öncesi):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre öncesi):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre öncesi)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre öncesi)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

            # Hiperparametre aralıkları
            params = {
                'C': [0.001, 0.01, 0.1, 1, 10, 100],
                'penalty': ['l1', 'l2']
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(logreg, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            logreg_model = LogisticRegression(**best_params)
            logreg_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = logreg_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre sonrası):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre sonrası):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre sonrası):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre sonrası):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre sonrası):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre sonrası):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre sonrası)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre sonrası)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

        # Regresyon işlemleri
        else:
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            st.write("Lojistik regresyon kullanarak regresyon yapmak uygun değildir. Lütfen başka bir algoritma seçin.")


    
    
elif page == "Mann-Whitney U Testi":
    import streamlit as st
    import pandas as pd
    from scipy.stats import mannwhitneyu

    
    def main():
        st.title("Mann Whitney U Testi 📊(İki Örnekli Wilcoxon Testi)")

        # Veri setini yükle
        allowed_formats = ["csv", "txt", "xls", "xlsx"]
        upload = st.file_uploader("İki örnekli veri setinizi CSV, TXT veya Excel formatında yükleyin", type=allowed_formats)

        if upload is not None:
            if "csv" in upload.name.lower():
                data = pd.read_csv(upload)
            elif "txt" in upload.name.lower():
                data = pd.read_csv(upload, delimiter='\t')
            elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
                data = pd.read_excel(upload)

            st.write("Veri Örneği:")
            st.write(data)

            # İki örnekli Wilcoxon testi için grup seçimi
            st.subheader("İki Örnekli Wilcoxon Testi için Gruplar")
            group1 = st.selectbox("Lütfen birinci grubu seçin:", data.columns)
            group2 = st.selectbox("Lütfen ikinci grubu seçin:", data.columns)

            # Mann-Whitney U testinin yapılması
            st.subheader("Mann-Whitney U Testi Sonuçları")
            stat, p_value = mannwhitneyu(data[group1], data[group2])
            st.write("Test İstatistiği:", stat)
            st.write("P-değeri:", p_value)

            # Sonuçların yorumlanması
            if p_value < 0.05:
                st.write("P-değeri 0.05 anlamlılık düzeyinden küçük olduğu için, gruplar arasında istatistiksel olarak anlamlı bir fark vardır.")
            else:
                st.write("P-değeri 0.05 anlamlılık düzeyinden büyük olduğu için, gruplar arasında istatistiksel olarak anlamlı bir fark yoktur.")

    if __name__ == "__main__":
        main()

    
    
elif page == "Random Forest":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    st.title("Random Forest 🔢")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # Random Forest sınıflandırma modeli oluşturma
            rf = RandomForestClassifier()
            rf.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = rf.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre öncesi):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre öncesi):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre öncesi):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre öncesi):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre öncesi):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre öncesi):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre öncesi)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre öncesi)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(rf, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            rf_model = RandomForestClassifier(**best_params)
            rf_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = rf_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre sonrası):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre sonrası):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre sonrası):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre sonrası):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre sonrası):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre sonrası):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre sonrası)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre sonrası)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # Random Forest regresyon modeli oluşturma
            rf = RandomForestRegressor()
            rf.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = rf.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu öncesi modelin kök ortalama kare hatası (RMSE):", rmse)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(rf, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            rf_model = RandomForestRegressor(**best_params)
            rf_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = rf_model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu sonrası modelin kök ortalama kare hatası (RMSE):", rmse)

    
    
    
elif page == "RBF SVM (Radial Basis Function Support Vector Machine)":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from sklearn.svm import SVC
    import matplotlib.pyplot as plt

    st.title("RBF SVM (Radial Basis Function Support Vector Machine)💹")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma işlemleri
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # RBF SVM sınıflandırma modeli oluşturma
        svm = SVC(kernel='rbf', probability=True)
        svm.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

        # Test verisi üzerinde modelin performansını değerlendirme
        y_pred = svm.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write("Doğruluk (Accuracy):", accuracy)

        precision = precision_score(y_test, y_pred)
        st.write("Hassasiyet (Precision):", precision)

        recall = recall_score(y_test, y_pred)
        st.write("Geri Çağırma (Recall):", recall)

        f1 = f1_score(y_test, y_pred)
        st.write("F1-Skor:", f1)

        roc_auc = roc_auc_score(y_test, y_pred)
        st.write("ROC AUC Skoru:", roc_auc)

        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_matrix_df = pd.DataFrame(conf_matrix,
                                    columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                    index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
        st.subheader("Karmaşıklık Matrisi:")
        st.write(conf_matrix_df)

        # ROC Eğrisi ve AUC Değeri
        fpr, tpr, thresholds = roc_curve(y_test, y_pred)
        plt.figure()
        plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Oranı')
        plt.ylabel('True Positive Oranı')
        plt.title('ROC Eğrisi')
        plt.legend(loc="lower right")
        st.pyplot(plt)

    
    
    
    
elif page == "SVC (Support Vector Classification)":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from sklearn.svm import SVC
    import matplotlib.pyplot as plt

    st.title("SVC (Support Vector Classification)💹")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma işlemleri
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # SVC sınıflandırma modeli oluşturma
        svc = SVC(probability=True)
        svc.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

        # Test verisi üzerinde modelin performansını değerlendirme
        y_pred = svc.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write("Doğruluk (Accuracy):", accuracy)

        precision = precision_score(y_test, y_pred)
        st.write("Hassasiyet (Precision):", precision)

        recall = recall_score(y_test, y_pred)
        st.write("Geri Çağırma (Recall):", recall)

        f1 = f1_score(y_test, y_pred)
        st.write("F1-Skor:", f1)

        roc_auc = roc_auc_score(y_test, y_pred)
        st.write("ROC AUC Skoru:", roc_auc)

        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_matrix_df = pd.DataFrame(conf_matrix,
                                    columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                    index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
        st.subheader("Karmaşıklık Matrisi:")
        st.write(conf_matrix_df)

        # ROC Eğrisi ve AUC Değeri
        fpr, tpr, thresholds = roc_curve(y_test, y_pred)
        plt.figure()
        plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Oranı')
        plt.ylabel('True Positive Oranı')
        plt.title('ROC Eğrisi')
        plt.legend(loc="lower right")
        st.pyplot(plt)


    
    
    
elif page == "XGBoost":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    from xgboost import XGBClassifier, XGBRegressor
    import matplotlib.pyplot as plt
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    st.title("XGBoost 📈")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # XGBoost sınıflandırma modeli oluşturma
            xgb = XGBClassifier()
            xgb.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = xgb.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre öncesi):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre öncesi):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre öncesi):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre öncesi):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre öncesi):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre öncesi):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre öncesi)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre öncesi)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(xgb, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            xgb_model = XGBClassifier(**best_params)
            xgb_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = xgb_model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write("Doğruluk (Accuracy) (Hiperparametre sonrası):", accuracy)

            precision = precision_score(y_test, y_pred)
            st.write("Hassasiyet (Precision) (Hiperparametre sonrası):", precision)

            recall = recall_score(y_test, y_pred)
            st.write("Geri Çağırma (Recall) (Hiperparametre sonrası):", recall)

            f1 = f1_score(y_test, y_pred)
            st.write("F1-Skor (Hiperparametre sonrası):", f1)

            roc_auc = roc_auc_score(y_test, y_pred)
            st.write("ROC AUC Skoru (Hiperparametre sonrası):", roc_auc)

            conf_matrix = confusion_matrix(y_test, y_pred)
            conf_matrix_df = pd.DataFrame(conf_matrix,
                                        columns=['Tahmin Edilen Negatif (0)', 'Tahmin Edilen Pozitif (1)'],
                                        index=['Gerçek Negatif (0)', 'Gerçek Pozitif (1)'])
            st.subheader("Karmaşıklık Matrisi (Hiperparametre sonrası):")
            st.write(conf_matrix_df)

            # ROC Eğrisi ve AUC Değeri (Hiperparametre sonrası)
            fpr, tpr, thresholds = roc_curve(y_test, y_pred)
            plt.figure()
            plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
            plt.plot([0, 1], [0, 1], 'k--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Oranı')
            plt.ylabel('True Positive Oranı')
            plt.title('ROC Eğrisi (Hiperparametre sonrası)')
            plt.legend(loc="lower right")
            st.pyplot(plt)

        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

            # XGBoost regresyon modeli oluşturma
            xgb = XGBRegressor()
            xgb.fit(X_train, y_train)  # Hiperparametre optimizasyonu öncesi modeli eğitme

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu öncesi)
            y_pred = xgb.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu öncesi modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu öncesi modelin kök ortalama kare hatası (RMSE):", rmse)

            # Hiperparametre aralıkları
            params = {
                'n_estimators': [100, 500, 1000],
                'learning_rate': [0.01, 0.05, 0.1],
                'max_depth': [3, 5, 7]
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(xgb, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            xgb_model = XGBRegressor(**best_params)
            xgb_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre optimizasyonu sonrası)
            y_pred = xgb_model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama kare hatası (MSE):", mse)

            mae = mean_absolute_error(y_test, y_pred)
            st.write("Hiperparametre optimizasyonu sonrası modelin ortalama mutlak hatası (MAE):", mae)

            rmse = mean_squared_error(y_test, y_pred, squared=False)
            st.write("Hiperparametre optimizasyonu sonrası modelin kök ortalama kare hatası (RMSE):", rmse)


    
    
    
elif page == "Yapay Sinir Ağları":
    import streamlit as st
    import pandas as pd
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import StandardScaler
    from sklearn.neural_network import MLPClassifier, MLPRegressor
    from sklearn.metrics import mean_squared_error, mean_absolute_error

    st.title("Yapay Sinir Ağları 🧠🕸️")

    # İzin verilen dosya formatları
    allowed_formats = ["csv", "txt", "xls", "xlsx"]

    # Kullanıcıdan veri yükleme
    upload = st.file_uploader("Veri setinizi CSV, TXT veya Excel formatında yükleyiniz.", type=allowed_formats)

    # Veri yüklendi mi kontrolü ve işlemler
    if upload is not None:
        if "csv" in upload.name.lower():
            df = pd.read_csv(upload)
        elif "txt" in upload.name.lower():
            df = pd.read_csv(upload, delimiter='\t')
        elif "xls" in upload.name.lower() or "xlsx" in upload.name.lower():
            df = pd.read_excel(upload)

        # Bağımsız ve bağımlı değişkenleri seçme
        st.subheader("Bağımsız ve Bağımlı Değişkenleri Seçme")
        X_options = df.select_dtypes(include=['number', 'float', 'int']).columns.tolist()  # Sayısal değişkenleri seç
        y_options = df.select_dtypes(include=['object', 'number', 'float', 'int']).columns.tolist()  # Kategorik değişkenleri seç
        X_selected = st.multiselect("Bağımsız Değişkenleri Seçin", X_options)
        y_selected = st.selectbox("Bağımlı Değişkeni Seçin", y_options)

        # Bağımsız ve bağımlı değişkenleri ayırma
        X = df[X_selected]
        y = df[y_selected]

        # Verilerin ölçeklendirilmesi
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Test verisi yüzdesi ve random state değeri girişi
        test_size = st.slider("Test verisi yüzdesi:", 0.1, 0.5, 0.2, 0.01)
        random_state = st.number_input("Random state değeri:", 0, 1000, 42, 1)
        st.write("----")

        # Sınıflandırma veya regresyon seçimi
        problem_type = st.radio("Problemi Seçin:", ("Sınıflandırma", "Regresyon"))

        # Sınıflandırma işlemleri
        if problem_type == "Sınıflandırma":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=random_state)

            # Yapay Sinir Ağı sınıflandırma modeli oluşturma
            ann = MLPClassifier(random_state=random_state)
            ann.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre öncesi)
            y_pred = ann.predict(X_test)
            accuracy_pre = accuracy_score(y_test, y_pred)
            precision_pre = precision_score(y_test, y_pred)
            recall_pre = recall_score(y_test, y_pred)
            f1_pre = f1_score(y_test, y_pred)
            roc_auc_pre = roc_auc_score(y_test, y_pred)

            # Hiperparametre aralıkları
            params = {
                'hidden_layer_sizes': [(100,), (50, 100), (50, 50, 50)],
                'activation': ['identity', 'logistic', 'tanh', 'relu'],
                'solver': ['lbfgs', 'sgd', 'adam']
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(ann, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            ann_model = MLPClassifier(**best_params, random_state=random_state)
            ann_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre sonrası)
            y_pred = ann_model.predict(X_test)
            accuracy_post = accuracy_score(y_test, y_pred)
            precision_post = precision_score(y_test, y_pred)
            recall_post = recall_score(y_test, y_pred)
            f1_post = f1_score(y_test, y_pred)
            roc_auc_post = roc_auc_score(y_test, y_pred)

            # Sonuçları gösterme
            st.write("Doğruluk (Accuracy) (Hiperparametre öncesi):", accuracy_pre)
            st.write("Hassasiyet (Precision) (Hiperparametre öncesi):", precision_pre)
            st.write("Geri Çağırma (Recall) (Hiperparametre öncesi):", recall_pre)
            st.write("F1-Skor (Hiperparametre öncesi):", f1_pre)
            st.write("ROC AUC Skoru (Hiperparametre öncesi):", roc_auc_pre)

            st.write("----")

            st.write("Doğruluk (Accuracy) (Hiperparametre sonrası):", accuracy_post)
            st.write("Hassasiyet (Precision) (Hiperparametre sonrası):", precision_post)
            st.write("Geri Çağırma (Recall) (Hiperparametre sonrası):", recall_post)
            st.write("F1-Skor (Hiperparametre sonrası):", f1_post)
            st.write("ROC AUC Skoru (Hiperparametre sonrası):", roc_auc_post)

        # Regresyon işlemleri
        elif problem_type == "Regresyon":
            # Veri kümesini eğitim ve test kümelerine ayırma
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=random_state)

            # Yapay Sinir Ağı regresyon modeli oluşturma
            ann = MLPRegressor(random_state=random_state)
            ann.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre öncesi)
            y_pred = ann.predict(X_test)
            mse_pre = mean_squared_error(y_test, y_pred)
            mae_pre = mean_absolute_error(y_test, y_pred)
            rmse_pre = mean_squared_error(y_test, y_pred, squared=False)

            # Hiperparametre aralıkları
            params = {
                'hidden_layer_sizes': [(100,), (50, 100), (50, 50, 50)],
                'activation': ['identity', 'logistic', 'tanh', 'relu'],
                'solver': ['lbfgs', 'sgd', 'adam']
            }

            # Hiperparametre optimizasyonu
            grid_search = GridSearchCV(ann, params, cv=5, n_jobs=-1, verbose=2)
            grid_search.fit(X_train, y_train)
            best_params = grid_search.best_params_

            st.write("En iyi parametreler:", best_params)

            # En iyi parametrelerle modeli tekrar eğitme
            ann_model = MLPRegressor(**best_params, random_state=random_state)
            ann_model.fit(X_train, y_train)

            # Test verisi üzerinde modelin performansını değerlendirme (hiperparametre sonrası)
            y_pred = ann_model.predict(X_test)
            mse_post = mean_squared_error(y_test, y_pred)
            mae_post = mean_absolute_error(y_test, y_pred)
            rmse_post = mean_squared_error(y_test, y_pred, squared=False)

            # Sonuçları gösterme
            st.write("Ortalama Kare Hata (MSE) (Hiperparametre öncesi):", mse_pre)
            st.write("Ortalama Mutlak Hata (MAE) (Hiperparametre öncesi):", mae_pre)
            st.write("Kök Ortalama Kare Hata (RMSE) (Hiperparametre öncesi):", rmse_pre)

            st.write("----")

            st.write("Ortalama Kare Hata (MSE) (Hiperparametre sonrası):", mse_post)
            st.write("Ortalama Mutlak Hata (MAE) (Hiperparametre sonrası):", mae_post)
            st.write("Kök Ortalama Kare Hata (RMSE) (Hiperparametre sonrası):", rmse_post)



