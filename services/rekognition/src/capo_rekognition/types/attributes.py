"""Generated from Smithy shape ``com.amazonaws.rekognition#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.attribute

Attributes: TypeAlias = list["capo_rekognition.types.attribute.Attribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Attributes) -> list:
    import capo_rekognition.types.attribute

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Attributes:
    import capo_rekognition.types.attribute

    out: Attributes = []
    for item in data:
        out.append(capo_rekognition.types.attribute.deserialize_aws_json_1_1(item))
    return out
