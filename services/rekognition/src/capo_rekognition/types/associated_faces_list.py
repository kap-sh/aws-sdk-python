"""Generated from Smithy shape ``com.amazonaws.rekognition#AssociatedFacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.associated_face

AssociatedFacesList: TypeAlias = list[
    "capo_rekognition.types.associated_face.AssociatedFace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatedFacesList) -> list:
    import capo_rekognition.types.associated_face

    out: list = []
    for item in value:
        out.append(capo_rekognition.types.associated_face.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociatedFacesList:
    import capo_rekognition.types.associated_face

    out: AssociatedFacesList = []
    for item in data:
        out.append(
            capo_rekognition.types.associated_face.deserialize_aws_json_1_1(item)
        )
    return out
