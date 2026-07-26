"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.face_id

FaceIdList: TypeAlias = list["capo_rekognition.types.face_id.FaceId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FaceIdList:
    return list(data)
