"""Generated from Smithy shape ``com.amazonaws.rekognition#Reasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.reason

Reasons: TypeAlias = list["aws_sdk_rekognition.types.reason.Reason"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Reasons) -> list:
    import aws_sdk_rekognition.types.reason

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.reason.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Reasons:
    import aws_sdk_rekognition.types.reason

    out: Reasons = []
    for item in data:
        out.append(aws_sdk_rekognition.types.reason.deserialize_aws_json_1_1(item))
    return out
