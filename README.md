# learning-101

Umbrella repo for the Automica **\*-101** learning family: one items/categories API shape, many stacks. Each project lives in its own GitHub repo and is included here as a **git submodule**.

Site catalogue: [automica.io/learning-101](https://automica.io/learning-101.html)

## Clone

```bash
git clone --recurse-submodules https://github.com/iammikek/learning-101.git
cd learning-101
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

```bash
make sync     # check out the commits pinned by this repo
make update   # fast-forward each submodule to origin/main (then commit new pins here if publishing)
make status   # submodule SHAs
```

## All projects

### Monolith backends (JSON API + `/shop`)

| Repo | Port | Stack |
|------|------|-------|
| [django-101](https://github.com/iammikek/django-101) | 8001 | Django + DRF |
| [framework-x-101](https://github.com/iammikek/framework-x-101) | 8004 | Framework X, ReactPHP |
| [laravel-101](https://github.com/iammikek/laravel-101) | 8003 | Laravel, Eloquent |
| [nativephp-101](https://github.com/iammikek/nativephp-101) | 8018 | NativePHP Mobile, Laravel |
| [orchestr-101](https://github.com/iammikek/orchestr-101) | 8005 | Orchestr, Ensemble |
| [rails-101](https://github.com/iammikek/rails-101) | 8012 | Rails 8, ActiveRecord |
| [symfony-101](https://github.com/iammikek/symfony-101) | 8002 | Symfony 7, Doctrine |

### API-only backends

| Repo | Port | Stack |
|------|------|-------|
| [cakephp-101](https://github.com/iammikek/cakephp-101) | 8017 | CakePHP 5, PHPUnit |
| [dotNet-101](https://github.com/iammikek/dotNet-101) | 8010 | ASP.NET Core, xUnit |
| [express-101](https://github.com/iammikek/express-101) | 8007 | Express, Vitest |
| [fastAPI-101](https://github.com/iammikek/fastAPI-101) | 8000 | FastAPI, SQLAlchemy |
| [flask-101](https://github.com/iammikek/flask-101) | 8011 | Flask, pytest |
| [fortran-101](https://github.com/iammikek/fortran-101) | 8008 | Fortran, fpm |
| [geblang-101](https://github.com/iammikek/geblang-101) | 8013 | Geblang, SQLite |
| [gebweb-101](https://github.com/iammikek/gebweb-101) | 8014 | Geblang + Gebweb |
| [go-101](https://github.com/iammikek/go-101) | 8000* | Gin, GORM |
| [java-101](https://github.com/iammikek/java-101) | 8009 | Spring Boot, JPA, Flyway |
| [nest-101](https://github.com/iammikek/nest-101) | 8006 | NestJS, TypeScript |
| [sinatra-101](https://github.com/iammikek/sinatra-101) | 8015 | Sinatra, RSpec |
| [slim-101](https://github.com/iammikek/slim-101) | 8016 | Slim 4, PHPUnit |

\* go-101 also uses port 8000 — run one backend at a time, or change the port in config.

### Clients

| Repo | Port / platform | Stack |
|------|-----------------|-------|
| [alpine-101](https://github.com/iammikek/alpine-101) | 5180 | Alpine.js, Vite |
| [flutter-101](https://github.com/iammikek/flutter-101) | mobile / desktop | Flutter |
| [react-101](https://github.com/iammikek/react-101) | 3000 | React 19, Vite |
| [vue-101](https://github.com/iammikek/vue-101) | 5173 | Vue 3, Pinia |

### Concept labs

| Repo | Stack |
|------|-------|
| [llm-101](https://github.com/iammikek/llm-101) | Offline-first Python LLM app exercises |

## Layout

Submodules are flat at the repo root, matching GitHub names (`framework-x-101`, `fastAPI-101`, …).

## Maintainer notes

- Pin submodules deliberately; do not force everyone onto floating `main` without a learning-101 commit.
- After changing a child repo: `git -C <name> pull origin main && git add <name> && git commit`.
- Site catalogue copy lives in [automica-public](https://github.com/iammikek/automica-public) (`src/learning-101.html`, `docs/learning-101.md`).
- Child READMEs link here for the family list; do not reintroduce full catalogue tables in individual repos.
