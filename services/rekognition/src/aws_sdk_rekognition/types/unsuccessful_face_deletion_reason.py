"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceDeletionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

UnsuccessfulFaceDeletionReason: TypeAlias = Literal[
    "ASSOCIATED_TO_AN_EXISTING_USER",
    "FACE_NOT_FOUND",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSOCIATED_TO_AN_EXISTING_USER",
        "FACE_NOT_FOUND",
    )
)


def serialize_aws_json_1_1(value: UnsuccessfulFaceDeletionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnsuccessfulFaceDeletionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UnsuccessfulFaceDeletionReason value: {data!r}"
        )
    return cast(UnsuccessfulFaceDeletionReason, data)
