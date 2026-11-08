# Esports Player Card

Веб-платформа с карточками игроков CS2 и Dota 2. Документы проекта лежат в папке `docs/`.

## Быстрый запуск (Windows, PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Открой файл `.env` и впиши пароль от PostgreSQL в `DB_PASSWORD`. Создай базу `playercard` (через pgAdmin: правая кнопка на «Databases» → Create → Database).

```powershell
py manage.py migrate
py manage.py runserver
```

Открой http://127.0.0.1:8000 в браузере.

## Тесты

```powershell
pytest
```

## Структура

- `config/` — настройки и главные адреса
- `apps/` — модули проекта (по одному на область)
- `templates/` — HTML-шаблоны
- `static/` — стили, скрипты, картинки интерфейса
- `tests/` — тесты
