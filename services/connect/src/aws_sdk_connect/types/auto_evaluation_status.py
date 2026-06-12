"""Generated from Smithy shape ``com.amazonaws.connect#AutoEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

AutoEvaluationStatus: TypeAlias = Literal[
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


def serialize_json(value: AutoEvaluationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoEvaluationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoEvaluationStatus value: {data!r}")
    return cast(AutoEvaluationStatus, data)
