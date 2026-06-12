"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDeletionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.unsuccessful_face_deletion

UnsuccessfulFaceDeletionsList: TypeAlias = list[
    "aws_sdk_rekognition.types.unsuccessful_face_deletion.UnsuccessfulFaceDeletion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDeletionsList) -> list:
    import aws_sdk_rekognition.types.unsuccessful_face_deletion

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_deletion.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnsuccessfulFaceDeletionsList:
    import aws_sdk_rekognition.types.unsuccessful_face_deletion

    out: UnsuccessfulFaceDeletionsList = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.unsuccessful_face_deletion.deserialize_aws_json_1_1(
                item
            )
        )
    return out
