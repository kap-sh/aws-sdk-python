"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDisassociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.unsuccessful_face_disassociation

UnsuccessfulFaceDisassociationList: TypeAlias = list[
    "aws_sdk_rekognition.types.unsuccessful_face_disassociation.UnsuccessfulFaceDisassociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDisassociationList) -> list:
    import aws_sdk_rekognition.types.unsuccessful_face_disassociation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_disassociation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsuccessfulFaceDisassociationList:
    import aws_sdk_rekognition.types.unsuccessful_face_disassociation

    out: UnsuccessfulFaceDisassociationList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_disassociation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
