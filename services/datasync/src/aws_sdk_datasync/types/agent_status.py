"""Generated from Smithy shape ``com.amazonaws.datasync#AgentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

AgentStatus: TypeAlias = Literal[
    "ONLINE",
    "OFFLINE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONLINE",
        "OFFLINE",
    )
)


def serialize_aws_json_1_1(value: AgentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatus value: {data!r}")
    return cast(AgentStatus, data)
