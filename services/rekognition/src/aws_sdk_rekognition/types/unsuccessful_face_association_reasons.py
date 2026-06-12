"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceAssociationReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.unsuccessful_face_association_reason

UnsuccessfulFaceAssociationReasons: TypeAlias = list[
    "aws_sdk_rekognition.types.unsuccessful_face_association_reason.UnsuccessfulFaceAssociationReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceAssociationReasons) -> list:
    import aws_sdk_rekognition.types.unsuccessful_face_association_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_association_reason.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsuccessfulFaceAssociationReasons:
    import aws_sdk_rekognition.types.unsuccessful_face_association_reason

    out: UnsuccessfulFaceAssociationReasons = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_association_reason.deserialize_aws_json_1_1(
                item
            )
        )
    return out
