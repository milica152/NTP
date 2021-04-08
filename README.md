# JSON structures manipulation and visualization

Aplikacija se pravi u jezicima Go, Python i Pharo.
Realizuje se Go biblioteka pomoću koje se manipuliše JSON fajlovima. Ona bi pružala CRUD operacije nad JSON fajlovima i time olakšala aplikacijama koje je koriste da skladište i manipulišu fajlovima u kojima se čuvaju stabla.
Realizuje se, takođe, mini DSL koji će služiti za pretragu stabala po zadatim parametrima.
Vizuelizacija objekata i njihove strukture bi bila napisana u jeziku Pharo.
Aplikacija koja sve to objedinjuje i omogućuje korisniku da koristi funkcionalnosti koje će biti navedene piše se u Python-u/Django. Takođe, kao proširenje generičke aplikacije koja manipuliše bilo kakvom strukturom JSON fajlova, biće realizovan i Django plug-in za specijalizaciju funkcionalnosti za porodična stabla.

Prototip aplikacije kada je korisnik ulogovan i kada mu je prikazan sadržaj izabranog fajla izgleda ovako:

![Screen 1@1x](https://user-images.githubusercontent.com/41242005/113946793-86492400-9809-11eb-9daa-9e884e64b6a0.png)

Aplikacija bi pružala nekoliko važnih funkcionalnosti (pored login-a i registracije korisnika), a koje su podeljene na sledeći način:

## Za projekat:
### Dodavanje novih članova u strukture

Dodavanje čvorova u već postojeće stablo je omogućeno klikom na dugme Add child (na slici). Pravljenjem takvog novog čvora bi se u fajlu iz kojeg je učitana struktura automatski napravila promena koju je korisnik načinio.

###  Brisanje postojećih članova iz strukture

Brisanje čvora se vrši klikom na dugme Delete (na slici). Nakon vršenja ove akcije čvor se pomoću napravljene biblioteke briše iz datoteke sa prethodnim upozorenjem korisnika.

### Čitanje JSON strukture iz fajla

Vrši se putem biblioteke i za specifičan fajl.

### Prikaz struktura (primer izgleda prikazane strukture na slici example.png)

Prikaz sturktura je interaktivan što znači da će korisnik moći da klikom na čvorove manipuliše njima i njihovim child čvorovima.

### Čuvanje novih struktura

Dodavanje novih struktura bi se realizovalo klikom na dugme NEW STRUCTURE (na slici), čime bi se kreirao i prikazao prazan graf sa mogućnošću dodavanja inicijalnog čvora.
Prilikom čuvanja novih struktura na specificiranom path-u pravi se fajl u kojem će se nalaziti sadržaj tog fajla.

### Izmena čvorova u JSON strukturi

Izmena parova ključ:vrednost koji pripadaju određenom čvoru se menja putem forme koja se otvara sa desne strane kada se klikne na čvor (na slici). Ova funkcionalnost je, takođe, podržana u biblioteci.

### Pregled sačuvanih struktura

Prikazuje do sada sačuvane strukture za svakog registrovanog korisnika.
Razlika u čuvanju grafova kada se radi o sačuvanom grafu za pojedinačnog korisnika i kada se radi samo o specificiranju lokalnog fajla za prikaz i obradu jeste što se strukture, odn. grafovi čuvaju na različitim mestima. Strukture koje nisu dosad sačuvane u korisnikovim strukturama (tab "My structures" na slici) će se birati iz lokalnog fajl sistema korisnika koji ih bira, a sačuvane strukture će se čuvati u okviru projekta. Za sačuvane strukture, zbog mogućnosti višekorisničkog režima rada, odn. mogućnosti da se korisnik prijavi na dva mesta na isti nalog, trebalo bi da se realizuje zaključavanje fajlova kojima se pristupa sve dok se ne završi pristupanje.

## Za diplomski:
### Pretraga čvorova prema željenim parametrima

Bio bi napravljen poseban DSL za pretragu struktura po određenim parametrima. DSL se ne bi razlikovao za pretrage porodičnog stabla i generičkih grafova, već bi ukoliko ne nađe ono što korisnik traži, vraćao određenu poruku.

### Plug-in za specijalizaciju porodičnih stabala

Sve navedene funkcionalnosti će biti omogućene i specijalizovane za porodična stabla preko plugin-a.
Plug-in bi proveravao da li tražena struktura odgovara strukturi porodičnog stabla (validacija ulaznih podataka) i time slao različite poruke biblioteci i programu za vizuelizaciju kako bi se oni ponašali drugačije u tom scenariju.
Plug-in bi preko interfejsa bio povezan sa aplikacijom i "override"-ovao gotovo sve generičke funkcionalnosti, a imao bi podatak o strukturi koju treba da poštuje porodično stablo.
