"""Generated from Smithy shape ``com.amazonaws.rekognition#CompareFacesUnmatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.compared_face

CompareFacesUnmatchList: TypeAlias = list[
    "capo_rekognition.types.compared_face.ComparedFace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompareFacesUnmatchList) -> list:
    import capo_rekognition.types.compared_face

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.compared_face.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CompareFacesUnmatchList:
    import capo_rekognition.types.compared_face

    out: CompareFacesUnmatchList = []
    for item in data:
        out.append(capo_rekognition.types.compared_face.deserialize_aws_json_1_1(item))
    return out
