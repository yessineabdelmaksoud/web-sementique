from rdflib import Graph, Namespace

# Charger le graphe RDF
g = Graph()
g.parse("ontology/education-tunisie.rdf")  # Vérifiez que le chemin est correct

# Définir le namespace
edu = Namespace("http://www.example.org/education-tunisie#")

# Requête SPARQL pour obtenir les établissements administrés par l'individu administratif "admin1"
query = """
PREFIX edu: <http://www.example.org/education-tunisie#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?admin ?etablissement
WHERE {
  ?admin rdf:type edu:Administratif .
  ?admin edu:administre ?etablissement .
  ?etablissement rdf:type edu:Établissements .
}
"""

# Exécuter la requête
results = g.query(query)

# Afficher les résultats
if results:
    for row in results:
        print(f"Établissement: {row.etablissement.split('#')[-1]}")
else:
    print("Aucun établissement trouvé.")
