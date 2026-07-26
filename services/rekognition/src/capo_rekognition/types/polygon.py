"""Generated from Smithy shape ``com.amazonaws.rekognition#Polygon``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.point

Polygon: TypeAlias = list["capo_rekognition.types.point.Point"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Polygon) -> list:
    import capo_rekognition.types.point

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.point.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Polygon:
    import capo_rekognition.types.point

    out: Polygon = []
    for item in data:
        out.append(capo_rekognition.types.point.deserialize_aws_json_1_1(item))
    return out
