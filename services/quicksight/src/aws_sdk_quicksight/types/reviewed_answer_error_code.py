"""Generated from Smithy shape ``com.amazonaws.quicksight#ReviewedAnswerErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ReviewedAnswerErrorCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "MISSING_ANSWER",
    "DATASET_DOES_NOT_EXIST",
    "INVALID_DATASET_ARN",
    "DUPLICATED_ANSWER",
    "INVALID_DATA",
    "MISSING_REQUIRED_FIELDS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "MISSING_ANSWER",
        "DATASET_DOES_NOT_EXIST",
        "INVALID_DATASET_ARN",
        "DUPLICATED_ANSWER",
        "INVALID_DATA",
        "MISSING_REQUIRED_FIELDS",
    )
)


def serialize_json(value: ReviewedAnswerErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ReviewedAnswerErrorCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewedAnswerErrorCode value: {data!r}")
    return cast(ReviewedAnswerErrorCode, data)
