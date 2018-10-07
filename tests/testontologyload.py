import unittest
import rdflib

from ontologymanager.ontology_manager import OntologyAPI


class OntologyLoadTest(unittest.TestCase):
    """Basic test cases."""

    def test_ontology_file_load(self):
        ontology_location = "../resources/edam.owl"
        loader = OntologyAPI(ontology_location)
        print(loader.getTopClasses())
        entities = loader.getAllNamedClasses()
        for e in entities:
            print(e)
            label_property = rdflib.URIRef("http://www.w3.org/2000/01/rdf-schema#label")
            annotations = loader.getValuesForGivenProperty(subject=e, property=label_property)
            for a in annotations: print(a.value)

if __name__ == '__main__':
    unittest.main()