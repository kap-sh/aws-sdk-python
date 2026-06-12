"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

AgentStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "RUNNING",
    "UNKNOWN",
    "BLACKLISTED",
    "SHUTDOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
        "RUNNING",
        "UNKNOWN",
        "BLACKLISTED",
        "SHUTDOWN",
    )
)


def serialize_aws_json_1_1(value: AgentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatus value: {data!r}")
    return cast(AgentStatus, data)
