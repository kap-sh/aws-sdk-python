"""Generated from Smithy shape ``com.amazonaws.opensearch#ActionSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

ActionSeverity: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "MEDIUM",
        "LOW",
    )
)


def serialize_json(value: ActionSeverity) -> str:
    return value


def deserialize_json(data: str) -> ActionSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionSeverity value: {data!r}")
    return cast(ActionSeverity, data)
