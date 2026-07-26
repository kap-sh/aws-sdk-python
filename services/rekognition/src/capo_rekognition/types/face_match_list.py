"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceMatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.face_match

FaceMatchList: TypeAlias = list["capo_rekognition.types.face_match.FaceMatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaceMatchList) -> list:
    import capo_rekognition.types.face_match

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.face_match.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FaceMatchList:
    import capo_rekognition.types.face_match

    out: FaceMatchList = []
    for item in data:
        out.append(capo_rekognition.types.face_match.deserialize_aws_json_1_1(item))
    return out
