"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_detail

FaceDetailList: TypeAlias = list["aws_sdk_rekognition.types.face_detail.FaceDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceDetailList) -> list:
    import aws_sdk_rekognition.types.face_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.face_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FaceDetailList:
    import aws_sdk_rekognition.types.face_detail

    out: FaceDetailList = []
    for item in data:
        out.append(aws_sdk_rekognition.types.face_detail.deserialize_aws_json_1_1(item))
    return out
