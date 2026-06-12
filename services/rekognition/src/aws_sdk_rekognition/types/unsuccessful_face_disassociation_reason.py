"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDisassociationReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

UnsuccessfulFaceDisassociationReason: TypeAlias = Literal[
    "FACE_NOT_FOUND",
    "ASSOCIATED_TO_A_DIFFERENT_USER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FACE_NOT_FOUND",
        "ASSOCIATED_TO_A_DIFFERENT_USER",
    )
)


def serialize_aws_json_1_1(value: UnsuccessfulFaceDisassociationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnsuccessfulFaceDisassociationReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UnsuccessfulFaceDisassociationReason value: {data!r}"
        )
    return cast(UnsuccessfulFaceDisassociationReason, data)
