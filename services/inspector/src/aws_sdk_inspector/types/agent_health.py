"""Generated from Smithy shape ``com.amazonaws.inspector#AgentHealth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector.errors import DeserializationError

AgentHealth: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: AgentHealth) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentHealth:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentHealth value: {data!r}")
    return cast(AgentHealth, data)
