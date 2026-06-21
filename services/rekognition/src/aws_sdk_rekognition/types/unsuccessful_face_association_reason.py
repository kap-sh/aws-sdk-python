"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceAssociationReason``."""

from typing import Literal, TypeAlias, cast

UnsuccessfulFaceAssociationReason: TypeAlias = Literal[
    "FACE_NOT_FOUND",
    "ASSOCIATED_TO_A_DIFFERENT_USER",
    "LOW_MATCH_CONFIDENCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceAssociationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnsuccessfulFaceAssociationReason:
    return cast(UnsuccessfulFaceAssociationReason, data)
