from rdflib import Graph, Namespace
#Enseignants et établissements où ils enseignent
# Charger le graphe RDF
g = Graph()
g.parse("ontology/education-tunisie.rdf")

# Définir le namespace
edu = Namespace("http://www.example.org/education-tunisie#")

# Requête SPARQL
query = """
PREFIX edu: <http://www.example.org/education-tunisie#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?enseignant ?etablissement
WHERE {
  ?enseignant a edu:Enseignant ;
              edu:enseigneDans ?etablissement .
}
"""

# Exécuter la requête
results = g.query(query)

# Afficher les résultats
for row in results:
    print(f"Enseignant: {row.enseignant.split('#')[-1]}, Établissement: {row.etablissement.split('#')[-1]}")
