"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face

FaceList: TypeAlias = list["aws_sdk_rekognition.types.face.Face"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceList) -> list:
    import aws_sdk_rekognition.types.face

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.face.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FaceList:
    import aws_sdk_rekognition.types.face

    out: FaceList = []
    for item in data:
        out.append(aws_sdk_rekognition.types.face.deserialize_aws_json_1_1(item))
    return out
