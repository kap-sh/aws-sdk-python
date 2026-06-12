"""Generated from Smithy shape ``com.amazonaws.rekognition#Assets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.asset

Assets: TypeAlias = list["aws_sdk_rekognition.types.asset.Asset"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Assets) -> list:
    import aws_sdk_rekognition.types.asset

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.asset.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Assets:
    import aws_sdk_rekognition.types.asset

    out: Assets = []
    for item in data:
        out.append(aws_sdk_rekognition.types.asset.deserialize_aws_json_1_1(item))
    return out
