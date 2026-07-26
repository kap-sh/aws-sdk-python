"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDisassociationReason``."""

from typing import Literal, TypeAlias, cast

UnsuccessfulFaceDisassociationReason: TypeAlias = Literal[
    "FACE_NOT_FOUND",
    "ASSOCIATED_TO_A_DIFFERENT_USER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsuccessfulFaceDisassociationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnsuccessfulFaceDisassociationReason:
    return cast(UnsuccessfulFaceDisassociationReason, data)
