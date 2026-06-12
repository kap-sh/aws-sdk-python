"""Generated from Smithy shape ``com.amazonaws.rekognition#Landmarks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.landmark

Landmarks: TypeAlias = list["aws_sdk_rekognition.types.landmark.Landmark"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Landmarks) -> list:
    import aws_sdk_rekognition.types.landmark

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.landmark.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Landmarks:
    import aws_sdk_rekognition.types.landmark

    out: Landmarks = []
    for item in data:
        out.append(aws_sdk_rekognition.types.landmark.deserialize_aws_json_1_1(item))
    return out
