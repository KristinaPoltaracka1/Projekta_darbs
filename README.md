# Projekta_darbs
## Produktu cenu salīdzināšana dažādos veikalos pēc Excel faila. 
Datorsistēmas kurss, 15. grupa. Autori: Kristina Poltaracka (231RDB084), Karolīna Buceneka (231RDB003), Stanislava Shulzhenko (2310RDB330)

### Projekta mērķis un tā darbība:
  Projekta darba galvenais mērķis ir izstrādāt programmu, kas veic efektīvu un precīzu produktu salīdzinājumu, sniedzot lietotājam informāciju par izdevīgākajiem un ekonomiski pieņemamākajiem produktu iegādes veidiem. Šajā analīzē tiek apskatīti divi no populārākajiem un biežāk apmeklētajiem veikaliem - Maxima un Rimi.
  
  Programma uzsāk darbību, atverot Rimi interneta veikalu un meklējot vēlamo preci, kuru lietotājs iepriekš ir atlasījis un norādījis Excel failā. Preces, kas atzīmētas ar "x" otrajā kolonā "Ņemu", tiek automātiski meklētas un pievienotas grozam Rimi interneta veikalā. Tāpat tiek ņemts vērā arī preču skaits, kas norādīts trešajā kolonā "Skaits".
  
  Pēc tam programma veic līdzīgu procesu ar Maxima (Barbora) interneta veikalu, taču, lai pievienotu preci, programma atceras preces cenu un tās daudzumu un pēc tam visu saskaita. Kad abiem veikaliem ir pievienotas visu nepieciešamo preci, programma radā kopējo summu, kuru lietotājam būtu jāsamaksā katrā veikalā. Beigās, izvadot informāciju terminālī, programma sniedz skaidru atbildi par to, kurā veikalā (Maximā vai Rimī) iegāde būtu izdevīgāka, piedāvājot lietotājam praktisku orientēšanās punktu iepirkuma izvēlē.

  Šī programma piedāvā lietotājiem ērtu un ātru veidu, kā salīdzināt un izvēlēties optimālo pirkumu vietu, ietaupot gan laiku, gan resursus.

### Izmantotās bibliotēkas:
  Selenium – Šī bibliotēka sniedz iespēju automatizēti mijiedarboties ar tīmekļa vietnēm, izmantojot Python programmu. Tas ir noderīgi strādājot ar datu iegūšanai no vietnēm vai darbību veikšanai tīmekļa formās. 
  > find = driver.find_element(By.ID, "search-input")

  Time – Šī bibliotēka nodrošina funkcijas laika apstrādei un aizkavei. Projektā tā tika izmantota, lai koordinētu darbības, kurām ir nepieciešama noteikta laika aizkave. 
  > piemēram: time.sleep(1)

  Pandas – Bibliotēka ļauj efektīvi strādāt ar dažādiem datiem, tostarp arī ar Excel failiem. Šī bibliotēka bija nepieciešama, lai apstrādātu un analizētu datus, ko iegūst no dažādām avotvietnēm vai veiktu sarežģītas datu manipulācijas. 
  > piemēram: fails = pandas.read_excel("Produkti.xlsx", sheet_name="Sheet1")
 




