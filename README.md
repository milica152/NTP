# FamilyTree application

Aplikacija se pravi u jezicima Go i Python. Realizuje se Go biblioteka pomoću koje se manipuliše JSON fajlovima. Ona bi pružala CRUD operacije nad JSON fajlovima i time olakšala aplikaciji FamilyTree da skladišti i manipuliše fajlovima u kojima se čuvaju stabla.

Aplikacija bi pružala nekoliko važnih funkcionalnosti (pored login-a i registracije korisnika):
- Dodavanje novih članova u porodično stablo u različitim ulogama (roditelj, dete, suprug, itd)
- Brisanje postojećih članova iz porodičnog stabla (realizovano kroz id kliknutog člana)
- Čitanje čitavog porodičnog stabla iz JSON fajla radi prikaza
- Pretraga članova prema njihovim atributima
- Prikaz porodičnog stabla (primer izgleda prikazanog stabla na slici example.png)
- Čuvanje porodičnih stabala (_My Trees_)
- Izmena članova u porodičnom stablu

Pretraga stabla se radi u posebno napravljenom mini-DSL jeziku.
Prikaz se radi u jeziku d3.
