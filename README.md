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

