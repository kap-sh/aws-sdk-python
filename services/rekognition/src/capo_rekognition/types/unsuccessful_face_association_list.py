"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.unsuccessful_face_association

UnsuccessfulFaceAssociationList: TypeAlias = list[
    "capo_rekognition.types.unsuccessful_face_association.UnsuccessfulFaceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceAssociationList) -> list:
    import capo_rekognition.types.unsuccessful_face_association

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.unsuccessful_face_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsuccessfulFaceAssociationList:
    import capo_rekognition.types.unsuccessful_face_association

    out: UnsuccessfulFaceAssociationList = []
    for item in data:
        out.append(
            capo_rekognition.types.unsuccessful_face_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
