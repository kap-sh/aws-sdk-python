"""Generated from Smithy shape ``com.amazonaws.rekognition#Instances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.instance

Instances: TypeAlias = list["aws_sdk_rekognition.types.instance.Instance"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Instances) -> list:
    import aws_sdk_rekognition.types.instance

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.instance.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Instances:
    import aws_sdk_rekognition.types.instance

    out: Instances = []
    for item in data:
        out.append(aws_sdk_rekognition.types.instance.deserialize_aws_json_1_1(item))
    return out
