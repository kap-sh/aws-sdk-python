"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDeletionReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.unsuccessful_face_deletion_reason

UnsuccessfulFaceDeletionReasons: TypeAlias = list[
    "capo_rekognition.types.unsuccessful_face_deletion_reason.UnsuccessfulFaceDeletionReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDeletionReasons) -> list:
    import capo_rekognition.types.unsuccessful_face_deletion_reason

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.unsuccessful_face_deletion_reason.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsuccessfulFaceDeletionReasons:
    import capo_rekognition.types.unsuccessful_face_deletion_reason

    out: UnsuccessfulFaceDeletionReasons = []
    for item in data:
        out.append(
            capo_rekognition.types.unsuccessful_face_deletion_reason.deserialize_aws_json_1_1(
                item
            )
        )
    return out
