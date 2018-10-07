import rdflib
from ontologymanager.ontology_manager import OntologyAPI
import json, requests
import urllib3

from wordsimilarity.semantic_enrichment import get_similar_word

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_ontology(ontology_location):
    '''
    Load ontology into memory
    :param ontology_location: file path to the ontology being loaded
    :return: ontology model loaded in memory
    '''
    # load ontology from above location into memory
    ontology = OntologyAPI(ontology_location)
    return ontology


def enrich_full_ontology_labels(ontology, label_property):
    '''
    find similar words for all labels in an ontology
    :param ontology: ontology loaded in memory
    :param label_property: the uri of the label
    :return:
    '''
    entities = ontology.getAllNamedClasses()
    results = {}
    for e in entities:
        annotations = ontology.getValuesForGivenProperty(subject=e, property=label_property)
        for a in annotations:
            results[a.value] = get_similar_word(a.value)
    return results


def enrich_ontology_labels_from_specific_parent(ontology, label_property, parent):
    '''
    find similar words for labels on a specific branch of an ontology based on a parent class
    :param ontology: ontology loaded in memory
    :param label_property: the uri of the label
    :param parent: the parent class for which all descendants (down to leaf nodes) will be extracted
    :return:
    '''
    entities = ontology.getDescendants(parent)
    print(entities)
    results = {}
    for e in entities:
        annotations = ontology.getValuesForGivenProperty(subject=e, property=label_property)
        for a in annotations:
            results[a.value] = get_similar_word(a.value)
    return results


def enrich_ontology_labels_for_class_siblings(ontology, label_property, sibling_class):
    '''
    find similar words for labels on a named class's siblings
    :param ontology: ontology loaded in memory
    :param label_property: the uri of the label
    :param parent: the parent class for which all descendants (down to leaf nodes) will be extracted
    :return:
    '''
    entities = ontology.getClassSiblings(sibling_class)
    print(entities)
    results = {}
    for e in entities:
        annotations = ontology.getValuesForGivenProperty(subject=e, property=label_property)
        for a in annotations:
            results[a.value] = get_similar_word(a.value)
    return results


if __name__ == '__main__':
    ontology_location = "../resources/edam.owl"
    #load ontology
    ontology = OntologyAPI(ontology_location)
    label_property = rdflib.URIRef("http://www.w3.org/2000/01/rdf-schema#label")

    #enrich a class's siblings
    results = enrich_ontology_labels_for_class_siblings(ontology, label_property, rdflib.URIRef("http://edamontology.org/format_3693"))
    print(json.dumps(results))

    #enrich part of an ontology based on the descendants (to leaf node) of a specific parent class
    results = enrich_ontology_labels_from_specific_parent(ontology, label_property, rdflib.URIRef("http://purl.obolibrary.org/obo/OBI_0100026"))
    print(json.dumps(results))

    #enrich a full ontology
    results = enrich_full_ontology_labels(ontology, label_property)
    print(json.dumps(results))



