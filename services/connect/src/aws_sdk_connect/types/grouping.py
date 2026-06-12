"""Generated from Smithy shape ``com.amazonaws.connect#Grouping``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

Grouping: TypeAlias = Literal[
    "QUEUE",
    "CHANNEL",
    "ROUTING_PROFILE",
    "ROUTING_STEP_EXPRESSION",
    "AGENT_STATUS",
    "SUBTYPE",
    "VALIDATION_TEST_TYPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUE",
        "CHANNEL",
        "ROUTING_PROFILE",
        "ROUTING_STEP_EXPRESSION",
        "AGENT_STATUS",
        "SUBTYPE",
        "VALIDATION_TEST_TYPE",
    )
)


def serialize_json(value: Grouping) -> str:
    return value


def deserialize_json(data: str) -> Grouping:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Grouping value: {data!r}")
    return cast(Grouping, data)
