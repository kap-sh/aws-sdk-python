"""Generated from Smithy shape ``com.amazonaws.rekognition#ComparedFaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.compared_face

ComparedFaceList: TypeAlias = list[
    "aws_sdk_rekognition.types.compared_face.ComparedFace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComparedFaceList) -> list:
    import aws_sdk_rekognition.types.compared_face

    out: list = []
    for item in value:
        out.append(aws_sdk_rekognition.types.compared_face.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ComparedFaceList:
    import aws_sdk_rekognition.types.compared_face

    out: ComparedFaceList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.compared_face.deserialize_aws_json_1_1(item)
        )
    return out
