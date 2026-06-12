"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationStatus: TypeAlias = Literal[
    "DRAFT",
    "SUBMITTED",
    "REVIEW_REQUESTED",
    "UNDER_REVIEW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "SUBMITTED",
        "REVIEW_REQUESTED",
        "UNDER_REVIEW",
    )
)


def serialize_json(value: EvaluationStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationStatus value: {data!r}")
    return cast(EvaluationStatus, data)
