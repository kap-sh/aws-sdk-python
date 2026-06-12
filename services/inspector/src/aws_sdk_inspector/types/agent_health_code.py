"""Generated from Smithy shape ``com.amazonaws.inspector#AgentHealthCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

AgentHealthCode: TypeAlias = Literal[
    "IDLE",
    "RUNNING",
    "SHUTDOWN",
    "UNHEALTHY",
    "THROTTLED",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDLE",
        "RUNNING",
        "SHUTDOWN",
        "UNHEALTHY",
        "THROTTLED",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: AgentHealthCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentHealthCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentHealthCode value: {data!r}")
    return cast(AgentHealthCode, data)
