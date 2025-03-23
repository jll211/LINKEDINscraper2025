# LinkedIn Scraper 2025

Modernes und robustes Tool zum Scrapen von LinkedIn-Daten, mit Fokus auf Sales Navigator und Recruiter-Funktionen. Dieses Repository enthält verbesserte Scripts für verschiedene LinkedIn-Scraping-Aufgaben.

## Hauptfunktionen

- **LinkedIn Sales Navigator Scraper**: Extrahiert Daten aus LinkedIn Sales Navigator Suchergebnissen
- **LinkedIn Recruiter Scraper**: Extrahiert Daten aus LinkedIn Recruiter Suchergebnissen
- **LinkedIn Profile Visitor**: Besucht LinkedIn-Profile automatisch und erzeugt so Besucherbenachrichtigungen

## Verbesserungen

- Robuste Authentifizierung mit Unterstützung für 2FA-Abfragen
- Automatische Erkennung des Endes von Ergebnislisten
- Zuverlässige Wartemechanismen mit WebDriverWait
- Bessere Fehlerbehandlung und Benutzerfeedback
- Automatisches Speichern der Ergebnisse im CSV- oder Excel-Format

## Einrichtung

1. Klone das Repository:
   ```bash
   git clone https://github.com/jll211/LINKEDINscraper2025.git
   cd LINKEDINscraper2025
   ```

2. Installiere die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

3. Erstelle die Datei `lk_credentials.json` mit deinen LinkedIn-Anmeldedaten:
   ```json
   {
       "email": "DEINE_LINKEDIN_EMAIL",
       "password": "DEIN_LINKEDIN_PASSWORT"
   }
   ```

4. Teste die Einrichtung:
   ```bash
   python test_setup.py
   ```

## Verwendung

### LinkedIn Sales Navigator Scraper

```bash
./run_sales_export.sh
```

Oder manuell:

```bash
python lksn_search_scraper.py --search-url "DEINE_SALES_NAVIGATOR_URL" --start-page 1 --end-page 999
```

### LinkedIn Profile Visitor

```bash
python lk_visitor.py --profile_file "sample_profiles.csv" --shortest_wait_time 5 --longest_wait_time 10
```

## Tipps

- Erhöhe die Wartezeiten, wenn LinkedIn dich blockiert
- Führe zuerst kleinere Tests durch, bevor du größere Scraping-Aufgaben startest
- Bei 2FA-Anforderungen folge den Anweisungen im Browser-Fenster

## Hinweis

Dieses Tool ist nur für Bildungszwecke gedacht. Die Nutzung muss in Übereinstimmung mit den LinkedIn-Nutzungsbedingungen erfolgen.