"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateAgentLogLevel``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: UpdateAgentLogLevel) -> str:
    return value


def deserialize_json(data: str) -> UpdateAgentLogLevel:
    return cast(UpdateAgentLogLevel, data)
