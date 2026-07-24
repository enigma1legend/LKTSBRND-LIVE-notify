# LKTSBRND-LIVE-notify

Öt percenként ellenőrzi GitHub Actionsön keresztül, hogy a `@jezusamegvalto`
TikTok-fiók élőben van-e, és ha igen (állapotváltozáskor), push értesítést
küld a telefonra ntfy.sh-n keresztül.

## Beállítás

1. **ntfy app a telefonra**: töltsd le az "ntfy" alkalmazást (Android: Google
   Play / F-Droid, iOS: App Store). Nyisd meg, és iratkozz fel egy általad
   kitalált, nehezen kitalálható topic névre, pl. `jezusamegvalto-live-a91f3c`
   (bárki, aki ismeri a topic nevet, tud rá üzenetet küldeni / olvasni, ezért
   ne legyen egyszerű).

2. **GitHub repó létrehozása**: hozz létre egy **publikus** repót (a publikus
   repóknál korlátlan az ingyenes Actions perckeret; privát repónál az 5
   perces ütemezés havonta könnyen túllépné az ingyenes 2000 percet).

3. **Kód feltöltése**: told fel ennek a mappának a tartalmát a repóba
   (lásd lentebb a git parancsokat).

4. **Secret hozzáadása**: a repóban *Settings → Secrets and variables →
   Actions → New repository secret*, név: `NTFY_TOPIC`, érték: az 1. pontban
   választott topic név (pl. `jezusamegvalto-live-a91f3c`).

5. **Tesztfuttatás**: a repó *Actions* fülén válaszd ki a "TikTok Live Check"
   workflow-t, és indítsd el kézzel (*Run workflow*), hogy lásd, működik-e.

Ezután a workflow 5 percenként automatikusan lefut, és amikor a state.json
szerinti "nem élő" állapotból "élő" állapotba vált a fiók, értesítést küld.

## Más felhasználó figyelése

A `.github/workflows/check-live.yml` fájlban a `TIKTOK_USERNAME` értékét kell
átírni.
