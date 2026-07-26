"""Generated from Smithy shape ``com.amazonaws.rekognition#ComparedFaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.compared_face

ComparedFaceList: TypeAlias = list["capo_rekognition.types.compared_face.ComparedFace"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparedFaceList) -> list:
    import capo_rekognition.types.compared_face

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.compared_face.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComparedFaceList:
    import capo_rekognition.types.compared_face

    out: ComparedFaceList = []
    for item in data:
        out.append(capo_rekognition.types.compared_face.deserialize_aws_json_1_1(item))
    return out
