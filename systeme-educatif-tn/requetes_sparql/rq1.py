from rdflib import Graph, Namespace, Literal

# Charger le graphe RDF
g = Graph()
g.parse("ontology/education-tunisie.rdf")

# Définir le namespace
edu = Namespace("http://www.example.org/education-tunisie#")

# Requête SPARQL
query = """
PREFIX edu: <http://www.example.org/education-tunisie#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?nom ?age ?etablissement ?filiere
WHERE {
  ?etudiant a edu:Étudiant ;
            edu:nom ?nom ;
            edu:age ?age ;
            edu:étudieDans ?etablissement ;
            edu:suitFormation ?formation .

  ?formation edu:aFiliere ?filiere .
}
"""

# Exécuter la requête
results = g.query(query)

# Afficher les résultats
for row in results:
    nom = str(row.nom)
    age = row.age.toPython()
    etablissement = str(row.etablissement.split("#")[-1])
    filiere = str(row.filiere.split("#")[-1])
    print(f"Nom: {nom}, Âge: {age}, Établissement: {etablissement}, Filière: {filiere}")
