"""Generated from Smithy shape ``com.amazonaws.comprehend#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity_type
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.list_of_block_references
    import aws_sdk_comprehend.types.string


class Entity(TypedDict, closed=True):
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""
    type: NotRequired["aws_sdk_comprehend.types.entity_type.EntityType"]
    """<p>The entity type. For entity detection using the built-in model, this field contains one of the standard entity types listed below.</p> <p>For custom entity detection, this field contains one of the entity types that you specified when you trained your custom model.</p>"""
    text: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>The text of the entity.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the first character in the entity.</p> <p>This field is empty for non-text input.</p>"""
    end_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the last character in the entity.</p> <p>This field is empty for non-text input.</p>"""
    block_references: NotRequired[
        "aws_sdk_comprehend.types.list_of_block_references.ListOfBlockReferences"
    ]
    """<p>A reference to each block for this entity. This field is empty for plain-text input.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entity) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "type" in value:
        import aws_sdk_comprehend.types.entity_type

        out["Type"] = aws_sdk_comprehend.types.entity_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "text" in value:
        out["Text"] = value["text"]
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    if "block_references" in value:
        import aws_sdk_comprehend.types.list_of_block_references

        out["BlockReferences"] = (
            aws_sdk_comprehend.types.list_of_block_references.serialize_aws_json_1_1(
                value["block_references"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "Score" in data:
        out["score"] = data["Score"]
    if "Type" in data:
        import aws_sdk_comprehend.types.entity_type

        out["type"] = aws_sdk_comprehend.types.entity_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Text" in data:
        out["text"] = data["Text"]
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    if "BlockReferences" in data:
        import aws_sdk_comprehend.types.list_of_block_references

        out["block_references"] = (
            aws_sdk_comprehend.types.list_of_block_references.deserialize_aws_json_1_1(
                data["BlockReferences"]
            )
        )
    return out
