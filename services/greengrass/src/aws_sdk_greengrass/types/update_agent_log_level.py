"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateAgentLogLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

"""The minimum level of log statements that should be logged by the OTA Agent during an update."""
UpdateAgentLogLevel: TypeAlias = Literal[
    "NONE",
    "TRACE",
    "DEBUG",
    "VERBOSE",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "TRACE",
        "DEBUG",
        "VERBOSE",
        "INFO",
        "WARN",
        "ERROR",
        "FATAL",
    )
)


def serialize_json(value: UpdateAgentLogLevel) -> str:
    return value


def deserialize_json(data: str) -> UpdateAgentLogLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateAgentLogLevel value: {data!r}")
    return cast(UpdateAgentLogLevel, data)
