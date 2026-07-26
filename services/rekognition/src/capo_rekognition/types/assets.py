"""Generated from Smithy shape ``com.amazonaws.rekognition#Assets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.asset

Assets: TypeAlias = list["capo_rekognition.types.asset.Asset"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Assets) -> list:
    import capo_rekognition.types.asset

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.asset.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Assets:
    import capo_rekognition.types.asset

    out: Assets = []
    for item in data:
        out.append(capo_rekognition.types.asset.deserialize_aws_json_1_1(item))
    return out
