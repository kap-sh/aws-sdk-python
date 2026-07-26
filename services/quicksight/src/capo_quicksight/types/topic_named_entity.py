"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNamedEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string
    import capo_quicksight.types.named_entity_definitions
    import capo_quicksight.types.semantic_entity_type
    import capo_quicksight.types.synonyms


class TopicNamedEntity(TypedDict, closed=True):
    entity_name: "capo_quicksight.types.limited_string.LimitedString"
    """<p>The name of the named entity.</p>"""
    entity_description: NotRequired[
        "capo_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The description of the named entity.</p>"""
    entity_synonyms: NotRequired["capo_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the named entity.</p>"""
    semantic_entity_type: NotRequired[
        "capo_quicksight.types.semantic_entity_type.SemanticEntityType"
    ]
    """<p>The type of named entity that a topic represents.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.named_entity_definitions.NamedEntityDefinitions"
    ]
    """<p>The definition of a named entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNamedEntity) -> dict:
    out: dict = {}
    out["EntityName"] = value["entity_name"]
    if "entity_description" in value:
        out["EntityDescription"] = value["entity_description"]
    if "entity_synonyms" in value:
        import capo_quicksight.types.synonyms

        out["EntitySynonyms"] = capo_quicksight.types.synonyms.serialize_json(
            value["entity_synonyms"]
        )
    if "semantic_entity_type" in value:
        import capo_quicksight.types.semantic_entity_type

        out["SemanticEntityType"] = (
            capo_quicksight.types.semantic_entity_type.serialize_json(
                value["semantic_entity_type"]
            )
        )
    if "definition" in value:
        import capo_quicksight.types.named_entity_definitions

        out["Definition"] = (
            capo_quicksight.types.named_entity_definitions.serialize_json(
                value["definition"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicNamedEntity:
    out: TopicNamedEntity = {}  # type: ignore[typeddict-item]
    if "EntityName" in data:
        out["entity_name"] = data["EntityName"]
    else:
        raise DeserializationError("TopicNamedEntity.entity_name required")
    if "EntityDescription" in data:
        out["entity_description"] = data["EntityDescription"]
    if "EntitySynonyms" in data:
        import capo_quicksight.types.synonyms

        out["entity_synonyms"] = capo_quicksight.types.synonyms.deserialize_json(
            data["EntitySynonyms"]
        )
    if "SemanticEntityType" in data:
        import capo_quicksight.types.semantic_entity_type

        out["semantic_entity_type"] = (
            capo_quicksight.types.semantic_entity_type.deserialize_json(
                data["SemanticEntityType"]
            )
        )
    if "Definition" in data:
        import capo_quicksight.types.named_entity_definitions

        out["definition"] = (
            capo_quicksight.types.named_entity_definitions.deserialize_json(
                data["Definition"]
            )
        )
    return out
