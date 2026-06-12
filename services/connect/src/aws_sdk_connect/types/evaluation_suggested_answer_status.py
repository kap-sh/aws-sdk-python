"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSuggestedAnswerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationSuggestedAnswerStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_json(value: EvaluationSuggestedAnswerStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationSuggestedAnswerStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EvaluationSuggestedAnswerStatus value: {data!r}"
        )
    return cast(EvaluationSuggestedAnswerStatus, data)
