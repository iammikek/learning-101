# learning-101

Umbrella repo for the Automica **\*-101** learning family: one items/categories API shape, many stacks. Each project lives in its own GitHub repo and is included here as a **git submodule**.

Catalogue: [automica.io/learning-101](https://automica.io/learning-101.html)

## Clone

```bash
git clone --recurse-submodules https://github.com/iammikek/learning-101.git
cd learning-101
```

If you already cloned without submodules:

```bash
git submodule update --init --recursive
```

Update every submodule to the commit pinned by this repo:

```bash
make sync
```

Pull latest `main` on every submodule (then commit the new pins in this repo if you want to publish them):

```bash
make update
```

## Layout

Submodules are flat at the repo root, matching GitHub names (`framework-x-101`, `fastAPI-101`, …).

| Kind | Projects |
|------|----------|
| **Monolith** (API + `/shop`) | django-101, framework-x-101, laravel-101, orchestr-101, rails-101, symfony-101 |
| **API-only** | dotNet-101, express-101, fastAPI-101, flask-101, fortran-101, geblang-101, gebweb-101, go-101, java-101, nest-101, sinatra-101, slim-101 |
| **Clients** | alpine-101, flutter-101, react-101, vue-101 |
| **Concept** | llm-101 |

Not yet published on GitHub (local only): `nativephp-101`, `python-101`. Add them as submodules when remotes exist.

## Ports (backends)

| Port | Repo |
|------|------|
| 8000 | fastAPI-101, go-101 |
| 8001 | django-101 |
| 8002 | symfony-101 |
| 8003 | laravel-101 |
| 8004 | framework-x-101 |
| 8005 | orchestr-101 |
| 8006 | nest-101 |
| 8007 | express-101 |
| 8008 | fortran-101 |
| 8009 | java-101 |
| 8010 | dotNet-101 |
| 8011 | flask-101 |
| 8012 | rails-101 |
| 8013 | geblang-101 |
| 8014 | gebweb-101 |
| 8015 | sinatra-101 |
| 8016 | slim-101 |

Clients: react-101 (3000), vue-101 (5173), alpine-101 (5180). flutter-101 has no fixed backend port.

## Maintainer notes

- Pin submodules deliberately; do not force everyone onto floating `main` without a learning-101 commit.
- After changing a child repo, from this repo: `git -C <name> pull origin main && git add <name> && git commit`.
- Site catalogue copy lives in [automica-public](https://github.com/iammikek/automica-public) (`src/learning-101.html`, `docs/learning-101.md`).
