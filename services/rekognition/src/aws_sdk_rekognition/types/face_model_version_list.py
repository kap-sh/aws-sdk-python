"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceModelVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string

FaceModelVersionList: TypeAlias = list["aws_sdk_rekognition.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceModelVersionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FaceModelVersionList:
    return list(data)
