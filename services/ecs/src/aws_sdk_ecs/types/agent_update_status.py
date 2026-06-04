"""Generated from Smithy shape ``com.amazonaws.ecs#AgentUpdateStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

AgentUpdateStatus: TypeAlias = Literal[
    "PENDING",
    "STAGING",
    "STAGED",
    "UPDATING",
    "UPDATED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "STAGING",
        "STAGED",
        "UPDATING",
        "UPDATED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: AgentUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentUpdateStatus value: {data!r}")
    return cast(AgentUpdateStatus, data)
