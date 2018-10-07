import json
import unittest
import rdflib

from ontologymanager.ontology_manager import OntologyAPI
from scibitemltk.synonym_suggestor_API import enrich_full_ontology_labels, enrich_ontology_labels_for_class_siblings, \
    enrich_ontology_labels_from_specific_parent


class OntologyEnrichmentTest(unittest.TestCase):
    """Basic test cases."""

    def test_enrich_full_ontology(self):
        ontology_location = "../resources/edam.owl"
        # load ontology
        ontology = OntologyAPI(ontology_location)
        label_property = rdflib.URIRef("http://www.w3.org/2000/01/rdf-schema#label")

        # enrich a full ontology
        results = enrich_full_ontology_labels(ontology, label_property)
        print(json.dumps(results))

    def test_enrich_class_siblings(self):
        ontology_location = "../resources/edam.owl"
        # load ontology
        ontology = OntologyAPI(ontology_location)
        label_property = rdflib.URIRef("http://www.w3.org/2000/01/rdf-schema#label")

        # enrich a class's siblings
        results = enrich_ontology_labels_for_class_siblings(ontology, label_property,
                                                            rdflib.URIRef("http://edamontology.org/format_3693"))
        print(json.dumps(results))

    def test_enrich_class_subbranch(self):
        ontology_location = "../resources/edam.owl"
        # load ontology
        ontology = OntologyAPI(ontology_location)
        label_property = rdflib.URIRef("http://www.w3.org/2000/01/rdf-schema#label")

        # enrich part of an ontology based on the descendants (to leaf node) of a specific parent class
        results = enrich_ontology_labels_from_specific_parent(ontology, label_property, rdflib.URIRef(
            "http://purl.obolibrary.org/obo/OBI_0100026"))
        print(json.dumps(results))