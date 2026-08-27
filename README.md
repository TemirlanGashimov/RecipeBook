# RecipeBook

RecipeBook ist eine Django-REST-API zum Verwalten von Rezepten. Rezepte enthalten einen Titel, eine Beschreibung, einen Erstellungszeitpunkt und einen Autor.

## Voraussetzungen

- Python 3.12 oder neuer
- Eine aktivierte virtuelle Umgebung

## Installation

Repository klonen oder in das Projektverzeichnis wechseln und anschließend eine virtuelle Umgebung erstellen:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Datenbankmigrationen ausführen:

```powershell
python manage.py migrate
```

Optional kann ein Admin-Benutzer angelegt werden:

```powershell
python manage.py createsuperuser
```

## Anwendung starten

```powershell
python manage.py runserver
```

Die API ist anschließend unter [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) erreichbar. Das Django-Admin-Interface befindet sich unter [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Authentifizierung

Alle API-Endpunkte benötigen eine Token-Authentifizierung. Für einen vorhandenen Benutzer kann im Django-Shell ein Token erstellt werden:

```powershell
python manage.py shell
```

```python
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.get(username="DEIN_BENUTZERNAME")
token, created = Token.objects.get_or_create(user=user)
print(token.key)
```

Das Token wird bei API-Anfragen im `Authorization`-Header übergeben:

```text
Authorization: Token DEIN_TOKEN
```

## API-Endpunkte

Basis-URL: `http://127.0.0.1:8000/api/recipes-list/`

| Methode | URL | Beschreibung |
|---|---|---|
| `GET` | `/api/recipes-list/` | Alle Rezepte abrufen |
| `POST` | `/api/recipes-list/` | Ein Rezept erstellen |
| `GET` | `/api/recipes-list/<id>/` | Ein Rezept abrufen |
| `PUT` | `/api/recipes-list/<id>/` | Ein Rezept vollständig aktualisieren |
| `PATCH` | `/api/recipes-list/<id>/` | Ein Rezept teilweise aktualisieren |
| `DELETE` | `/api/recipes-list/<id>/` | Ein Rezept löschen |

Beispiel für eine Anfrage zum Erstellen eines Rezepts:

```powershell
curl.exe -X POST http://127.0.0.1:8000/api/recipes-list/ `
  -H "Authorization: Token DEIN_TOKEN" `
  -H "Content-Type: application/json" `
  -d '{"title":"Pizza","description":"Tunfisch Pizza","author":1}'
```

Die API liefert folgende Rezeptfelder zurück:

- `id`
- `title`
- `description`
- `created_at`
- `author`

## Tests

Die Tests werden mit Django ausgeführt:

```powershell
python manage.py test
```

## Projektstruktur

```text
core/                Django-Projekt und Einstellungen
recipes_app/         Rezepte-App
recipes_app/api/     Serializer, Views und API-Routen
recipes_app/tests/   API-Tests
db.sqlite3           SQLite-Datenbank
manage.py            Django-Verwaltungsskript
requirements.txt     Python-Abhängigkeiten
```
