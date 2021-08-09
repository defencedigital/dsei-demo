# How to run this demo

## Create a demo Web App
Some Mark Down text files are used as the basis for an MKDocs site.
```
site_name: DSEI 21 Demo
site_description: 'DSEI 21 Demo'
site_author: 'Defence Digital Foundry'
docs_dir: docs/
repo_name: 'defencedigital/dsei-demo'
repo_url: 'https://github.com/defencedigital/dsei-demo'
nav:
    - Home: index.md
    - How To: howto.md
theme:
  name: material
  palette:
    scheme: default
    primary: deep purple
    accent: deep orange
```

### Use GH Pages to host the original site
Git Hub Pages using Actions
```
name: 'GitHub Pages'
on:
  push:
    branches:
      - main
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.x
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

## Create a container
Also create a container with the site contents using actions and push to quay.io container registry.
