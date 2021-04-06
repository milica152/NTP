# JSON structures manipulation and visualization

Aplikacija se pravi u jezicima Go, Python i Pharo.
Realizuje se Go biblioteka pomoću koje se manipuliše JSON fajlovima. Ona bi pružala CRUD operacije nad JSON fajlovima i time olakšala aplikacijama koje je koriste da skladište i manipulišu fajlovima u kojima se čuvaju stabla.
Realizuje se, takođe, mini DSL koji će služiti za pretragu stabala po zadatim parametrima.
Vizuelizacija objekata i njihove strukture bi bila napisana u jeziku Pharo.
Aplikacija koja sve to objedinjuje i omogućuje korisniku da koristi funkcionalnosti koje će biti navedene piše se u Python-u/Django. Takođe, kao proširenje generičke aplikacije koja manipuliše bilo kakvom strukturom JSON fajlova, biće realizovan i Django plug-in za specijalizaciju funkcionalnosti za porodična stabla.

Aplikacija bi pružala nekoliko važnih funkcionalnosti (pored login-a i registracije korisnika), a koje su podeljene na sledeći način:

Za projekat:
- Dodavanje novih članova u strukture
- Brisanje postojećih članova iz strukture
- Čitanje JSON strukture iz fajla
- Prikaz porodičnog stabla (primer izgleda prikazanog stabla na slici example.png)
- Čuvanje novih struktura
- Izmena čvorova u JSON strukturi
- Pregled sačuvanih struktura, prikazuje do sada sačuvane strukture i realizuje se za svakog registrovanog korisnika pojedinačno 

Za diplomski:
- Pretraga članova prema njihovim atributima
- Plug-in za specijalizaciju za porodičnim stablima (sve navedene funkcionalnosti prilagođene strukturi porodičnog stabla)
