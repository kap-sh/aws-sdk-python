"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityLabel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.pii_entity_type


class EntityLabel(TypedDict):
    name: NotRequired["aws_sdk_comprehend.types.pii_entity_type.PiiEntityType"]
    """<p>The name of the label.</p>"""
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The level of confidence that Amazon Comprehend has in the accuracy of the detection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityLabel) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_comprehend.types.pii_entity_type

        out["Name"] = aws_sdk_comprehend.types.pii_entity_type.serialize_aws_json_1_1(
            value["name"]
        )
    if "score" in value:
        out["Score"] = value["score"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityLabel:
    out: EntityLabel = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_comprehend.types.pii_entity_type

        out["name"] = aws_sdk_comprehend.types.pii_entity_type.deserialize_aws_json_1_1(
            data["Name"]
        )
    if "Score" in data:
        out["score"] = data["Score"]
    return out
