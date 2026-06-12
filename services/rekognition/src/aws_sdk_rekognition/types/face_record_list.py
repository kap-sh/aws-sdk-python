"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.face_record

FaceRecordList: TypeAlias = list["aws_sdk_rekognition.types.face_record.FaceRecord"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceRecordList) -> list:
    import aws_sdk_rekognition.types.face_record

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.face_record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FaceRecordList:
    import aws_sdk_rekognition.types.face_record

    out: FaceRecordList = []
    for item in data:
        out.append(aws_sdk_rekognition.types.face_record.deserialize_aws_json_1_1(item))
    return out
