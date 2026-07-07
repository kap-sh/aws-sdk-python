"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.pii_entity_type


class PiiEntity(TypedDict, closed=True):
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""
    type: NotRequired["aws_sdk_comprehend.types.pii_entity_type.PiiEntityType"]
    """<p>The entity's type.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the first character in the entity.</p>"""
    end_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The zero-based offset from the beginning of the source text to the last character in the entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntity) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "type" in value:
        import aws_sdk_comprehend.types.pii_entity_type

        out["Type"] = aws_sdk_comprehend.types.pii_entity_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PiiEntity:
    out: PiiEntity = {}  # type: ignore[typeddict-item]
    if "Score" in data:
        out["score"] = data["Score"]
    if "Type" in data:
        import aws_sdk_comprehend.types.pii_entity_type

        out["type"] = aws_sdk_comprehend.types.pii_entity_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    return out
