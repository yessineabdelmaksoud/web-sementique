from rdflib import Graph, Namespace
#Étudiants et leur cycle d'études

# Charger le graphe RDF
g = Graph()
g.parse("ontology/education-tunisie.rdf")

# Définir le namespace
edu = Namespace("http://www.example.org/education-tunisie#")

# Requête SPARQL
query = """
PREFIX edu: <http://www.example.org/education-tunisie#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?nom ?cycle
WHERE {
  ?etudiant a edu:Étudiant ;
            edu:nom ?nom ;
            edu:suitFormation ?formation .
  ?formation edu:aCycle ?cycle .
}
"""

# Exécuter la requête
results = g.query(query)

# Afficher les résultats
for row in results:
    print(f"Nom: {row.nom}, Cycle: {row.cycle.split('#')[-1]}")
