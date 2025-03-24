#!/bin/bash
# LinkedIn Sales Navigator Search Export Script

# Die URL der Suche (mit Unternehmen, die Finanzierungsrunden in den letzten 12 Monaten erhalten haben)
SEARCH_URL="https://www.linkedin.com/sales/search/company?query=(filters%3AList((type%3AACCOUNT_ACTIVITIES%2Cvalues%3AList((id%3ARFE%2Ctext%3AFinanzierungsrunden%2520in%2520den%2520vergangenen%252012%2520Monaten%2CselectionType%3AINCLUDED)))))&sessionId=8MZtD4V8Qmi4R5Up64qTQQ%3D%3D&viewAllFilters=true"

# Seitenzahlen definieren - Startseite 1, End-Seite auf einen sehr hohen Wert setzen,
# damit der Scraper so lange läuft, bis keine weiteren Seiten mehr verfügbar sind
START_PAGE=1
END_PAGE=999

# Wartezeiten optimieren, um Blockierungen zu vermeiden
WAIT_BETWEEN_PAGES=8
WAIT_AFTER_LOADING=5
WAIT_AFTER_SCROLL=4

echo "Starte LinkedIn Sales Navigator Scraper..."
echo "URL: $SEARCH_URL"
echo "Scraping aller verfügbaren Seiten (bis zu Seite $END_PAGE)"
echo ""

# Führe den Sales Navigator Scraper aus
python lksn_search_scraper.py \
  --search-url "$SEARCH_URL" \
  --start-page $START_PAGE \
  --end-page $END_PAGE \
  --wait-time-between-pages $WAIT_BETWEEN_PAGES \
  --wait-after-page-loaded $WAIT_AFTER_LOADING \
  --wait-after-scroll-down $WAIT_AFTER_SCROLL \
  --save-format "csv"

echo ""
echo "Wenn eine Zwei-Faktor-Authentifizierung erforderlich ist, bitte im Browser bestätigen."
echo "Die Ergebnisse werden im Verzeichnis 'lksn_data' gespeichert."
echo "Der Scraper stoppt automatisch, wenn keine weiteren Seiten verfügbar sind."