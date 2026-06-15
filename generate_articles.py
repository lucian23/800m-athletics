import re

with open('/tmp/800m-athletics/index.html','r',encoding='utf-8') as f:
    html = f.read()

new_articles = [
    ("🇷🇴", "Istorie", "800m în România — de la începuturi la performanțe mondiale", "Istoria probei de 800 de metri în atletismul românesc reflectă evoluția sportului de performanță din țara noastră. Primele competiții organizate datează de la începutul secolului XX, iar proba de 800m a devenit rapid una dintre disciplinele de referință. Atleți romani au reprezentat țara cu mândrie la campionate europene, mondiale și olimpice, lăsând o amprentă importantă asupra istoriei atletismului românesc."),
    ("🥇", "Campioni", "Ovidiu Olteanu — campion balcanic de 800m", "Ovidiu Olteanu este unul dintre cei mai valoroși semifondiști romani, medaliat la multiple ediții ale Campionatelor Balcanice. Stilul său de alergare, bazat pe o tactică inteligentă și un finish puternic, l-a făcut remarcat în competițiile regionale. Cariera sa exemplifică dedicarea necesară pentru a excela la proba de 800m pe plan internațional."),
    ("🏅", "Recorduri", "Recordul național de 800m pentru bărbați", "Recordul național de 800m la bărbați este o bornă importantă a atletismului românesc. Fiecare generație de semifondiști a încercat să coboare această barieră, iar lupta pentru record național a generat rivalități memorabile pe pistă. Valoarea recordului reflectă nivelul performanței din țara noastră comparativ cu elita mondială."),
    ("🏃‍♀️", "Recorduri", "Recordul național de 800m pentru femei", "La fel ca la bărbați, recordul național feminin de 800m este urmărit cu mare interes. Atletele române au avut performanțe notabile pe plan internațional, iar semifondul a fost o probă unde România a produs constant talente capabile să concureze la nivel înalt."),
    ("🏟️", "Competiții", "Campionatele Naționale de atletism — proba de 800m", "Campionatele Naționale de atletism reprezintă momentul culminant al sezonului competițional românesc. Proba de 800m este una dintre cele mai spectaculoase, adesea decisă în ultimii 50 de metri. Atât seniorii, cât și tinerii sportivi privesc Naționalele ca șansa de a-și confirma evoluția și de a obține selecții în loturile naționale."),
    ("🌟", "Tineret", "Descoperirea tinerelor talente la 800m", "Descoperirea și dezvoltarea tinerelor talente pentru proba de 800m începe în școli și cluburi locale. Antrenorii caută copii cu aptitudini pentru viteză și rezistență, apoi îi introduc treptat în specificul semifondului. Programul de selecție și competițiile pentru cadeți și juniori sunt esențiale pentru viitorul atletismului românesc."),
    ("🧑‍🏫", "Antrenament", "Rolul antrenorului în dezvoltarea unui semifondist", "Antrenorul de atletism este mai mult decât un creator de planuri de antrenament. El este psiholog, strateg și mentor. Pentru un semifondist de 800m, antrenorul trebuie să găsească echilibrul perfect între volum aerob, viteză, forță și recuperare, adaptând continuu planul la progresele și provocările sportivului."),
    ("📊", "Știință", "Testarea în laborator a atleților de 800m", "Testarea de laborator — VO2 max, prag lactic, analiza compoziției corporale — oferă date esențiale pentru programarea antrenamentului. În România, centrele de medicină sportivă și kinetoterapie contribuie la evaluarea periodică a sportivilor de performanță, ajutând la prevenirea accidentărilor și optimizarea pregătirii."),
    ("🩺", "Sănătate", "Cele mai frecvente accidentări la 800m", "Semifondiștii sunt expuși unor accidentări specifice: tendinite, probleme la nivelul gambelor, dureri de spate și stres osos. Majoritatea pot fi prevenite printr-o încălzire corespunzătoare, antrenament progresiv, forță corect executată și recuperare adecvată. Ignorarea semnalelor de alarmă duce adesea la pauze lungi din activitate."),
    ("🍎", "Nutriție", "Dieta zilnică a unui atlet de 800m", "O dietă echilibrată pentru un semifondist include carbohidrați pentru energie, proteine pentru refacere, grăsimi sănătoase și micronutrienți esențiali. Mesele regulate, hidratarea constantă și evitarea alimentelor procesate sunt principii de bază. Fiecare atlet trebuie să-și personalizeze dieta în funcție de volumul de antrenament și obiectivele de greutate corporală."),
    ("💊", "Suplimente", "Suplimente alimentare utile pentru semifondiști", "Suplimentele pot juca un rol auxiliar, dar niciodată înlocuitor al alimentației. Creatina, beta-alanina, cofeina și electroliții sunt printre cele mai studiate și utilizate în sportul de anduranță-viteză. Întotdeauna trebuie administrate sub supraveghere și în conformitate cu reglementările antidoping."),
    ("🧘", "Mental", "Pregătirea mentală înainte de o cursă importantă", "Pregătirea mentală este la fel de importantă ca cea fizică. Tehnici de respirație, vizualizare, rutine pre-cursă și reframingul anxietății în entuziasm pot transforma performanța. Atleții de elită investesc ani în dezvoltarea rezilienței psihice, știind că ultimii 100 de metri sunt câștigați în minte."),
    ("⏲️", "Tactica", "Cum să alergi primii 200 de metri în 800m", "Primii 200 de metri stabilesc ritmul și poziția în grup. Pornirea prea tare poate duce la acumularea rapidă a lactatului, în timp ce o ieșire prea lentă poate bloca atletul în spatele plutonului. Strategia optimă este un start puternic dar controlat, care permite menținerea unui ritm susținut pe următorii 600 de metri."),
    ("🔄", "Tactica", "Cum să gestionezi al doilea tur în 800m", "Al doilea tur este unde se decide cursa. După primii 400m, lactatul crește, iar ritmul pare din ce în ce mai greu. Alergătorii disciplinați mențin o alergare eficientă tehnic, folosesc brațele pentru propulsie și încep să pregătească atacul final în ultimii 150-200 de metri."),
    ("🚀", "Tactica", "Sprintul final în proba de 800m", "Sprintul final de 800m este unul dintre cele mai spectaculoase momente din atletism. Cu mușchii plini de acid lactic, atletul trebuie să găsească resurse pentru o accelerare decisivă. Antrenamentul specific pentru finish — repetări scurte după efort prealabil — este esențial pentru a dezvolta această capacitate."),
    ("🏋️‍♂️", "Forță", "Forța core — stabilizatorul alergătorului", "Un core puternic stabilizează trunchiul în timpul alergării, îmbunătățește transferul de forță și reduce riscul de accidentări la nivelul spatelui. Exerciții precum plank, dead bug, hollow body și rotații anti-rotation sunt ideale pentru atleți și pot fi incluse de 2-3 ori pe săptămână."),
    ("🦵", "Forță", "Exerciții pentru gambă și tendonul lui Ahile", "Gamba și tendonul lui Ahile absorb forțe enorme în timpul sprintului. Întărirea lor progresivă — prin sărituri în gambe, ridicări pe vârfuri, și exerciții de amortizare controlată — reduce riscul de tendinită și ruptură. Recuperarea după aceste exerciții trebuie respectată cu strictețe."),
    ("🏃", "Tehnica", "Tehnica de alergare pentru 800m", "O tehnică eficientă de alergare economisește energie și previne accidentări. Elementele cheie sunt: pas ușor și rapid, contact scurt cu solul, brațe relaxate dar active, umerii coborâți, privirea înainte și respirație ritmică. Semifondiștii trebuie să-și mențină tehnica chiar și sub oboseală."),
    ("🌡️", "Recuperare", "Contrastul rece-cald în recuperarea atleților", "Terapia prin contrast — alternarea apei reci cu cea caldă sau utilizarea băilor de gheață — ajută la reducerea inflamației și accelerarea recuperării. Utilizată corect după antrenamente intense, această metodă poate reduce durerile musculare și poate îmbunătăți calitatea antrenamentelor ulterioare."),
    ("🛌", "Recuperare", "Masajul și automasajul pentru semifondiști", "Masajul terapeutic îmbunătățește circulația, reduce tensiunea musculară și grăbește eliminarea lactatului. Atleții pot învăța tehnici simple de automasaj cu ajutorul rolelor de spumă sau a mingilor de masaj, aplicându-le zilnic pe grupele musculare solicitate."),
    ("📈", "Planificare", "Periodizarea anuală pentru 800m", "Periodizarea înseamnă împărțirea anului în blocuri cu obiective specifice: bază, precompetițional, competițional și tranziție. Fiecare fază are propriul volum, intensitate și accent. O periodizare bine făcută duce la un vârf de formă exact în momentul competițiilor importante."),
    ("🧪", "Testare", "Time trial-urile ca instrument de progres", "Time trial-urile — curse contra cronometru în antrenament — sunt un instrument esențial pentru monitorizarea progresului. Ele simulează presiunea competiției fără costul unei competiții reale. Un atlet de 800m poate folosi time trial-uri lunare pentru a-și ajusta ritmurile-țintă și pentru a evalua eficacitatea planului de antrenament."),
    ("🎯", "Obiective", "Cum să-ți stabilești obiective SMART în atletism", "Obiectivele SMART — Specifice, Măsurabile, Atinse, Relevante, Limitate în timp — ajută atleții să rămână focalizați. În loc de vreau să alerg mai repede, un obiectiv bun este vreau să cobor timpul la 800m sub 2:00 până în luna iulie. Astfel de ținte clarifică antrenamentul și motivează progresul."),
    ("🎽", "Echipament", "Alegerea echipamentului de alergare pentru vară", "Vara, alegerea echipamentului corect devine crucială. Haine ușoare, respirabile, care evacuează transpirația, șosete tehnice anti-bășică și ochelari de soare pentru antrenamentele de dimineață sunt recomandări esențiale. Evită bumbacul, care reține umezeala și crește riscul de iritații."),
    ("🧤", "Echipament", "Echipament de alergare pentru iarnă", "Iarna, layering-ul este cheia: strat de bază termic, strat izolant și strat exterior rezistent la vânt. Mănuși, căciulă și pantaloni lungi tehnici protejează extremitățile. Nu uita de vizibilitate — îmbrăcăminte reflectorizantă sau lumini pentru antrenamentele în întuneric."),
    ("📚", "Istorie", "Marii rivali ai probei de 800m", "Istoria 800m este marcată de rivalități epice: Sebastian Coe vs Steve Ovett, Wilson Kipketer vs Vebjørn Rodal, David Rudisha vs toți ceilalți. Aceste confruntări au ridicat nivelul probei și au inspirat generații întregi de alergători. Rivalitățile sănătoase demonstrează că progresul este accelerați de concurență."),
    ("🌍", "Internațional", "Evoluția recordului mondial feminin de 800m", "Recordul mondial feminin de 800m, deținut de Jarmila Kratochvílová din 1983, rămâne unul dintre cele mai longevive și discutate recorduri din atletism. Discuțiile despre acest record reflectă evoluția eticii sportive și a regulamentelor antidoping. Pe lângă acesta, performanțele moderne ale atletelor africane și americane au ridicat continuu nivelul probei."),
    ("🇰🇪", "Campioni", "Tradiția kenyană la 800m", "Kenya a produs unii dintre cei mai mari semifondiști din istorie, de la Kipchoge Keino la David Rudisha și Emmanuel Wanyonyi. Tradiția kenyană combină altitudinea, cultura alergării, antrenamentele în grup și o mentalitate de învingători. Studierea acestui model oferă lecții valoroase pentru atleții și antrenorii din întreaga lume."),
    ("🧒", "Tineret", "Cum să începi proba de 800m la 12-14 ani", "La vârste fragede, copiii nu trebuie suprasolicitați cu antrenamente specifice de viteză-viteză. Începutul trebuie să se bazeze pe multilateralitate, jocuri, alergare ușoară și dezvoltarea coordonării. Specializarea în 800m devine relevantă abia în adolescență târzie, când sistemele energetice sunt mai mature."),
    ("🏫", "Educație", "Atletismul școlar și proba de 800m", "La nivel școlar, proba de 800m este una dintre disciplinele standard ale olimpiadelor și concursurilor interșcolare. Mulți campioni romani au descoperit atletismul exact în aceste competiții. Profesorii de educație fizică joacă un rol esențial în identificarea și îndrumarea primelor talente."),
    ("🏥", "Sănătate", "Monitorizarea pulsului în antrenamentele de 800m", "Monitorizarea frecvenței cardiace ajută la controlul intensității și la prevenirea supraantrenamentului. Zona aerobă, zona de prag și zona de viteză maximă au fiecare un rol în programul unui semifondist. Un ceas cu GPS și monitor de puls este un instrument util pentru antrenamente moderne."),
    ("⚖️", "Nutriție", "Managementul greutății pentru alergători", "Greutatea corporală influențează direct economia de alergare. Un atlet de 800m trebuie să-și mențină o greutate stabilă, optimă pentru putere și rezistență, fără diete extreme. Pierderea rapidă în greutate slăbește forța și crește riscul de îmbolnăvire. Schimbările trebuie făcute gradual, sub supraveghere."),
    ("🌙", "Recuperare", "Importanța zilelor de odihnă", "Zilele de odihnă nu sunt zile pierdute — sunt zile în care corpul se adaptează la antrenament. Fără odihnă suficientă, progresul este anulat de supraantrenament. Un program inteligent alternează zilele grele cu zilele ușoare sau de repaus activ, respectând semnalele corpului."),
    ("🔬", "Știință", "Rolul lactatului în performanța de 800m", "Acidul lactic este adesea perceput ca inamicul atletului, dar el este de fapt un combustibil. Problema apare când lactatul se acumulează mai repede decât poate fi eliminat. Antrenamentul specific crește toleranța la lactat și capacitatea de a funcționa la niveluri ridicate de aciditate musculară."),
    ("🎵", "Mental", "Muzica și motivația în antrenament", "Muzica poate crește motivația și poate reduce percepția efortului în antrenamentele de volum sau de forță. Tempoul rapid și mesajele motivaționale ajută în sesiunile repetitive. Cu toate acestea, pentru antrenamentele de tehnică sau pentru perioadele de concentrare maximă, liniștea poate fi mai benefică."),
    ("🗓️", "Competiții", "Calendarul competițional internațional de 800m", "Calendarul de 800m include campionate naționale, balcanice, europene, mondiale și Jocurile Olimpice. Fiecare competiție are cerințe de calificare, iar planificarea sezonului trebuie sincronizată cu aceste termene. Atleții și antrenorii urmăresc minimele de calificare și selectează competițiile potrivite obiectivelor."),
    ("🏅", "Campioni", "Doina Melinte — o legendă a atletismului românesc", "Doina Melinte este una dintre cele mai mari atlete române din istorie, medaliată olimpică și multiplă campioană europeană la 800m. Cariera sa impresionantă a inspirat generații de sportive și a ridicat prestigiul atletismului românesc pe plan internațional. Dedicarea, inteligența tactică și calitățile fizice excepționale au făcut-o o campioană de legendă."),
    ("📱", "Tehnologie", "Aplicații și gadgeturi pentru monitorizarea antrenamentului", "În era digitală, atleții folosesc aplicații pentru logarea antrenamentelor, analiza ritmului, somnului și recuperării. Gadgeturi precum ceasurile GPS, inelele inteligente și senzorii de putere oferă date valoroase. Important este însă ca tehnologia să complementeze, nu să înlocuiască, simțul antrenorului și experiența sportivului."),
    ("🥦", "Nutriție", "Micul dejun ideal pentru un atlet de 800m", "Micul dejun stabilește energia pentru întreaga zi. O masă echilibrată include carbohidrați complecși (ovăz, pâine integrală), proteine (ouă, iaurt grecesc), fructe și o sursă de grăsimi sănătoase (nuci, avocado). Evită dulciurile și produsele de patiserie, care provoacă fluctuații de energie."),
    ("🦶", "Tehnica", "Biomecanica pasului în 800m", "Biomecanica alergării de 800m se află la intersecția dintre sprint și fond. Frecvența pasului, lungimea pasului, timpul de contact cu solul și unghiul de propulsie trebuie optimizate pentru eficiență. Analiza video a alergării poate ajuta antrenorul și sportivul să identifice și corecteze deficiențele tehnice."),
    ("🧊", "Recuperare", "Somnul și hormonul de creștere la atleți", "Somnul de calitate stimulează eliberarea hormonului de creștere, esențial pentru refacerea musculară. Atleții de 800m, care solicită intens sistemul muscular și nervos, au nevoie de 8-10 ore de somn. Calitatea somnului este la fel de importantă ca durata — un mediu întunecat, răcoros și fără ecrane favorizează somnul profund."),
    ("🌅", "Antrenament", "Antrenamentele de dimineață pentru 800m", "Antrenamentele de dimineață pot fi benefice pentru dezvoltarea rezistenței aerobe și pentru obișnuirea corpului cu efortul în stare de repaus glicemic. Cu toate acestea, sesiunile intense de viteză sunt mai eficiente după-amiaza, când temperatura corporală și coordonarea sunt la maxim. Planificarea zilei trebuie să țină cont de aceste ritmuri."),
    ("📰", "Noutăți", "Trenduri moderne în antrenamentul de 800m", "Antrenamentul modern de 800m combină știința, tehnologia și tradiția. Trenduri actuale includ utilizarea intervalelor polarizate, monitorizarea HRV pentru recuperare, antrenamentul la altitudine și integrarea forței funcționale. Atleții și antrenorii români pot adopta treptat aceste metode pentru a rămâne competitivi."),
]

insert_marker = "                    </article>\n\n                </div>\n            </div>\n        </section>\n\n        <!-- Antrenamente Section -->"

insert_pos = html.find(insert_marker)
if insert_pos == -1:
    raise Exception("Could not find insert marker")

new_html_articles = ""
for i, (icon, cat, title, body) in enumerate(new_articles, start=14):
    paragraphs = body.split('\n')
    body_html = "\n                            ".join(f"<p>{p}</p>" for p in paragraphs)
    new_html_articles += f"""                    <!-- Article {i} -->
                    <article class="news-card">
                        <div class="news-image"><div class="placeholder-image">{icon}</div></div>
                        <div class="news-content">
                            <span class="news-category">{cat}</span>
                            <h3>{title}</h3>
                            <p>{paragraphs[0][:160]}...</p>
                            <a href="#" class="read-more">Citește mai mult →</a>
                        </div>
                        <div class="article-full">
                            {body_html}
                        </div>
                    </article>

"""

new_html = html[:insert_pos] + "\n" + new_html_articles + html[insert_pos:]

new_html = new_html.replace(
    '<span class="stat-number">2</span>\n                        <span class="stat-label">Tururi de pistă</span>',
    '<span class="stat-number">52</span>\n                        <span class="stat-label">Articole</span>'
)
new_html = new_html.replace(
    'Resursă completă pentru atleții de 800m - antrenamente, strategii, nutriție și noutăți',
    '800m.ro - Resursă completă pentru atleții de 800m. Peste 50 de articole despre antrenamente, strategii, nutriție și istoria atletismului românesc.'
)
new_html = new_html.replace(
    '800m, atletism, antrenament, alergare, mijloc, strategie cursă',
    '800m, atletism romanesc, atletism, antrenament, alergare, mijloc, strategie cursa, semifond, Romania'
)

with open('/tmp/800m-athletics/index.html','w',encoding='utf-8') as f:
    f.write(new_html)

article_count = len(re.findall(r'<article class="news-card">', new_html))
print(f"Total articole: {article_count}")
print(f"Lungime index.html: {len(new_html)} bytes")
