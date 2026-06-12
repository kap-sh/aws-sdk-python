"""Generated from Smithy shape ``com.amazonaws.rekognition#UnsuccessfulFaceAssociationReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

UnsuccessfulFaceAssociationReason: TypeAlias = Literal[
    "FACE_NOT_FOUND",
    "ASSOCIATED_TO_A_DIFFERENT_USER",
    "LOW_MATCH_CONFIDENCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FACE_NOT_FOUND",
        "ASSOCIATED_TO_A_DIFFERENT_USER",
        "LOW_MATCH_CONFIDENCE",
    )
)


def serialize_aws_json_1_1(value: UnsuccessfulFaceAssociationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnsuccessfulFaceAssociationReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UnsuccessfulFaceAssociationReason value: {data!r}"
        )
    return cast(UnsuccessfulFaceAssociationReason, data)
