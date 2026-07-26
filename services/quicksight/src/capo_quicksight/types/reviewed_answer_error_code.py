"""Generated from Smithy shape ``com.amazonaws.quicksight#ReviewedAnswerErrorCode``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ReviewedAnswerErrorCode) -> str:
    return value


def deserialize_json(data: str) -> ReviewedAnswerErrorCode:
    return cast(ReviewedAnswerErrorCode, data)
