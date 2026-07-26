"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDeletionReason``."""

from typing import Literal, TypeAlias, cast

UnsuccessfulFaceDeletionReason: TypeAlias = Literal[
    "ASSOCIATED_TO_AN_EXISTING_USER",
    "FACE_NOT_FOUND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDeletionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnsuccessfulFaceDeletionReason:
    return cast(UnsuccessfulFaceDeletionReason, data)
