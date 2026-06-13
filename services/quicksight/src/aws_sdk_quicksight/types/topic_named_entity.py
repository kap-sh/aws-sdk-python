"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicNamedEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.named_entity_definitions
    import aws_sdk_quicksight.types.semantic_entity_type
    import aws_sdk_quicksight.types.synonyms


class TopicNamedEntity(TypedDict):
    entity_name: "aws_sdk_quicksight.types.limited_string.LimitedString"
    """<p>The name of the named entity.</p>"""
    entity_description: NotRequired[
        "aws_sdk_quicksight.types.limited_string.LimitedString"
    ]
    """<p>The description of the named entity.</p>"""
    entity_synonyms: NotRequired["aws_sdk_quicksight.types.synonyms.Synonyms"]
    """<p>The other names or aliases for the named entity.</p>"""
    semantic_entity_type: NotRequired[
        "aws_sdk_quicksight.types.semantic_entity_type.SemanticEntityType"
    ]
    """<p>The type of named entity that a topic represents.</p>"""
    definition: NotRequired[
        "aws_sdk_quicksight.types.named_entity_definitions.NamedEntityDefinitions"
    ]
    """<p>The definition of a named entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicNamedEntity) -> dict:
    out: dict = {}
    out["EntityName"] = value["entity_name"]
    if "entity_description" in value:
        out["EntityDescription"] = value["entity_description"]
    if "entity_synonyms" in value:
        import aws_sdk_quicksight.types.synonyms

        out["EntitySynonyms"] = aws_sdk_quicksight.types.synonyms.serialize_json(
            value["entity_synonyms"]
        )
    if "semantic_entity_type" in value:
        import aws_sdk_quicksight.types.semantic_entity_type

        out["SemanticEntityType"] = (
            aws_sdk_quicksight.types.semantic_entity_type.serialize_json(
                value["semantic_entity_type"]
            )
        )
    if "definition" in value:
        import aws_sdk_quicksight.types.named_entity_definitions

        out["Definition"] = (
            aws_sdk_quicksight.types.named_entity_definitions.serialize_json(
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
        import aws_sdk_quicksight.types.synonyms

        out["entity_synonyms"] = aws_sdk_quicksight.types.synonyms.deserialize_json(
            data["EntitySynonyms"]
        )
    if "SemanticEntityType" in data:
        import aws_sdk_quicksight.types.semantic_entity_type

        out["semantic_entity_type"] = (
            aws_sdk_quicksight.types.semantic_entity_type.deserialize_json(
                data["SemanticEntityType"]
            )
        )
    if "Definition" in data:
        import aws_sdk_quicksight.types.named_entity_definitions

        out["definition"] = (
            aws_sdk_quicksight.types.named_entity_definitions.deserialize_json(
                data["Definition"]
            )
        )
    return out
