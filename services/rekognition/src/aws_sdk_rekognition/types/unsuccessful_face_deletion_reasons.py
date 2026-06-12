"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDeletionReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.unsuccessful_face_deletion_reason

UnsuccessfulFaceDeletionReasons: TypeAlias = list[
    "aws_sdk_rekognition.types.unsuccessful_face_deletion_reason.UnsuccessfulFaceDeletionReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDeletionReasons) -> list:
    import aws_sdk_rekognition.types.unsuccessful_face_deletion_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_deletion_reason.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsuccessfulFaceDeletionReasons:
    import aws_sdk_rekognition.types.unsuccessful_face_deletion_reason

    out: UnsuccessfulFaceDeletionReasons = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_deletion_reason.deserialize_aws_json_1_1(
                item
            )
        )
    return out
