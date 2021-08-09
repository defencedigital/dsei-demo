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
```
name: 'Build and Push Image'
on:
  push:
    branches:
      - main

jobs:
  job_1:
    name: 'MKDocs Build'
    runs-on: ubuntu-latest
    steps:
      - name: 'mkdocs build'
        uses: actions/checkout@v2
      - run: |
          pip install -r requirements.txt
          mkdocs build
      - name: 'upload site'
        uses: actions/upload-artifact@v2
        with:
          name: dsei-site
          path: site

  job_2:
    name: 'Create Container'
    needs: job_1
    runs-on: ubuntu-latest
    steps:
      - name: 'checkout'
        uses: actions/checkout@v2
      - name: 'download artifact'
        uses: actions/download-artifact@v2
        with:
          name: dsei-site
          path: site
      - name: 'list folders'
        run: |
          sudo apt-get -y install tree
          tree
      - name: 'Build Container'
        id: build-image
        uses:  redhat-actions/buildah-build@v2
        with:
          image: dsei-demo
          tags: latest ${{ github.sha }}
          dockerfiles: |
            ./Containerfile
      - name: Push To quay.io
        id: push-to-quay
        uses: redhat-actions/push-to-registry@v2
        with:
          image: ${{ steps.build-image.outputs.image }}
          tags: ${{ steps.build-image.outputs.tags }}
          registry: quay.io/defencedigital
          username: ${{ secrets.REGISTRY_USER }}
          password: ${{ secrets.REGISTRY_PASSWORD }}

      - name: Print image url
        run: echo "Image pushed to ${{ steps.push-to-quay.outputs.registry-paths }}"
```
