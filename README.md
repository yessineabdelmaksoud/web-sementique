# web-sementique
 # 🧠 Ontologie du Système Éducatif en Tunisie

## 📌 Phase 1 : Choix du domaine

### 🎯 Domaine choisi : Système Éducatif en Tunisie

L'objectif de ce projet est de modéliser le **système éducatif tunisien** à travers une ontologie formelle permettant de représenter les **acteurs**, les **établissements**, ainsi que les **cycles et filières de formation**.

### ✅ Justification du choix

Le domaine de l'éducation en Tunisie est :
- **Structuré** : il existe des catégories bien définies (étudiants, enseignants, cycles d'études, etc.).
- **Pertinent** : il a un impact direct sur la société et l'économie tunisiennes.
- **Riche en données** : de nombreuses sources (ministère, universités, statistiques, etc.) permettent de valider le modèle.
- **Utile** : l'ontologie peut servir à construire des systèmes d’information intelligents pour la gestion de parcours étudiants, de programmes de formation, ou pour la recherche scientifique.

---

## 🧱 Concepts clés identifiés

L'ontologie est structurée selon trois dimensions principales : les personnes, les établissements, et les formations.

### 🧑‍🏫 1. Personnes
Représente les acteurs humains impliqués dans le système éducatif :
- **Étudiant** : inscrit dans une filière, suit un cycle de formation.
- **Enseignant** : enseigne dans un établissement et dans une filière.
- **Administratif** : gère des tâches au sein des établissements.

### 🏛️ 2. Établissements
Types d'établissements où se déroule l'enseignement :
- **Université**
- **Institut Supérieur**
- **Lycée**

### 🎓 3. Formation
Représente les parcours académiques et leurs spécialisations :
- **Cycle** :
  - Licence
  - Master
  - Doctorat
- **Filière** :
  - Informatique
  - Médecine
  - Génie Civil

---

## 🌳 Hiérarchie du domaine

```text
Système Éducatif Tunisien
├── Personnes
│   ├── Étudiant
│   ├── Enseignant
│   └── Administratif
├── Établissements
│   ├── Université
│   ├── Institut Supérieur
│   └── Lycée
└── Formation
    ├── Cycle
    │   ├── Licence
    │   ├── Master
    │   └── Doctorat
    └── Filière
        ├── Informatique
        ├── Médecine
        └── Génie Civil
## 🧱 Phase 2 : Modélisation RDF / RDFS avec Protégé

Nous avons modélisé l'ontologie à l'aide du logiciel **Protégé**.

### 📚 Namespaces utilisés

| Préfixe | URI |
|--------|-----|
| `rdf`  | http://www.w3.org/1999/02/22-rdf-syntax-ns# |
| `rdfs` | http://www.w3.org/2000/01/rdf-schema# |
| `xsd`  | http://www.w3.org/2001/XMLSchema# |
| `owl`  | http://www.w3.org/2002/07/owl# |

---

### 🧩 Classes créées

- **Personne**
  - Étudiant
  - Enseignant
  - Administratif
- **Établissement**
  - Université
  - Institut Supérieur
  - Lycée
- **Formation**
  - Cycle (Licence, Master, Doctorat)
  - Filière (Informatique, Médecine, Génie Civil)

---

### 🔁 Propriétés object

| Nom propriété    | Domaine        | Portée (Range)   |
|------------------|----------------|------------------|
| `étudieDans`     | Étudiant       | Établissement    |
| `enseigneDans`   | Enseignant     | Établissement    |
| `administre`     | Administratif  | Établissement    |
| `suitFormation`  | Étudiant       | Formation        |
| `aCycle`         | Formation      | Cycle            |
| `aFiliere`       | Formation      | Filière          |

---

### 🔤 Propriétés data

| Nom propriété         | Domaine   | Type de données |
|-----------------------|-----------|------------------|
| `nom`                 | Personne  | `xsd:string`     |
| `age`                 | Étudiant  | `xsd:integer`    |
| `annéeInscription`    | Étudiant  | `xsd:gYear`      |

---

### 👤 Individus ajoutés

- **Étudiant1**
- **Etab1**
- **Institut1**

> Ces individus ont été définis dans Protégé et enregistrés au format RDF.

---

### 🖼️ Captures d’écran

> Voici quelques captures d’écran montrant la structure de l’ontologie dans Protégé :

#### 1. Vue des classes
![Vue des classes](../capture/classe.png)

#### 2. Propriétés objet
![Propriétés objet](./captures/proprietes_objet.png)

#### 3. Propriétés de données
![Propriétés de données](./captures/proprietes_data.png)

#### 4. Individus créés
![Individus](./captures/individus.png)

> 📁 **Remarque** : les images doivent être placées dans un dossier `/captures/` dans le même répertoire que le fichier `README.md`.

---

### 💾 Export

Le fichier RDF a été sauvegardé sous le nom :  
📄 `systeme_educatif.rdf`

---

## ✅ Résultat

- Ontologie modélisée avec classes, propriétés, et individus
- Sauvegarde au format RDF
- Prêt pour la phase suivante : **requêtes SPARQL**

---
