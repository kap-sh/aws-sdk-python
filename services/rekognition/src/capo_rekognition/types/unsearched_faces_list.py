"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsearchedFacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.unsearched_face

UnsearchedFacesList: TypeAlias = list[
    "capo_rekognition.types.unsearched_face.UnsearchedFace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsearchedFacesList) -> list:
    import capo_rekognition.types.unsearched_face

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.unsearched_face.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UnsearchedFacesList:
    import capo_rekognition.types.unsearched_face

    out: UnsearchedFacesList = []
    for item in data:
        out.append(
            capo_rekognition.types.unsearched_face.deserialize_aws_json_1_1(item)
        )
    return out
