"""Generated from Smithy shape ``com.amazonaws.rekognition#Labels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.label

Labels: TypeAlias = list["aws_sdk_rekognition.types.label.Label"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Labels) -> list:
    import aws_sdk_rekognition.types.label

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.label.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Labels:
    import aws_sdk_rekognition.types.label

    out: Labels = []
    for item in data:
        out.append(aws_sdk_rekognition.types.label.deserialize_aws_json_1_1(item))
    return out
