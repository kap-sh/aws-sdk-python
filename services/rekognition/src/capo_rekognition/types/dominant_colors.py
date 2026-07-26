"""Generated from Smithy shape ``com.amazonaws.rekognition#DominantColors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.dominant_color

DominantColors: TypeAlias = list["capo_rekognition.types.dominant_color.DominantColor"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DominantColors) -> list:
    import capo_rekognition.types.dominant_color

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.dominant_color.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DominantColors:
    import capo_rekognition.types.dominant_color

    out: DominantColors = []
    for item in data:
        out.append(capo_rekognition.types.dominant_color.deserialize_aws_json_1_1(item))
    return out
