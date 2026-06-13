"""Generated from Smithy shape ``com.amazonaws.bedrock#ReasoningEffort``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ReasoningEffort: TypeAlias = Literal[
    "low",
    "medium",
    "high",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "low",
        "medium",
        "high",
    )
)


def serialize_json(value: ReasoningEffort) -> str:
    return value


def deserialize_json(data: str) -> ReasoningEffort:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReasoningEffort value: {data!r}")
    return cast(ReasoningEffort, data)
