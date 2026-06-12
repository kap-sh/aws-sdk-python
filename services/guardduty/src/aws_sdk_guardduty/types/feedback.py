"""Generated from Smithy shape ``com.amazonaws.guardduty#Feedback``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

Feedback: TypeAlias = Literal[
    "USEFUL",
    "NOT_USEFUL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USEFUL",
        "NOT_USEFUL",
    )
)


def serialize_json(value: Feedback) -> str:
    return value


def deserialize_json(data: str) -> Feedback:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Feedback value: {data!r}")
    return cast(Feedback, data)
