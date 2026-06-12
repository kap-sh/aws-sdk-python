"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDisassociationReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.unsuccessful_face_disassociation_reason

UnsuccessfulFaceDisassociationReasons: TypeAlias = list[
    "aws_sdk_rekognition.types.unsuccessful_face_disassociation_reason.UnsuccessfulFaceDisassociationReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDisassociationReasons) -> list:
    import aws_sdk_rekognition.types.unsuccessful_face_disassociation_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_disassociation_reason.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsuccessfulFaceDisassociationReasons:
    import aws_sdk_rekognition.types.unsuccessful_face_disassociation_reason

    out: UnsuccessfulFaceDisassociationReasons = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_disassociation_reason.deserialize_aws_json_1_1(
                item
            )
        )
    return out
