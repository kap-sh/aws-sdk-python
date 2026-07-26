"""Generated from Smithy shape ``com.amazonaws.rekognition#DisassociatedFacesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.disassociated_face

DisassociatedFacesList: TypeAlias = list[
    "capo_rekognition.types.disassociated_face.DisassociatedFace"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociatedFacesList) -> list:
    import capo_rekognition.types.disassociated_face

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.disassociated_face.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DisassociatedFacesList:
    import capo_rekognition.types.disassociated_face

    out: DisassociatedFacesList = []
    for item in data:
        out.append(
            capo_rekognition.types.disassociated_face.deserialize_aws_json_1_1(item)
        )
    return out
