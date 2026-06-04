"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedAgentName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ManagedAgentName: TypeAlias = Literal["ExecuteCommandAgent",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ExecuteCommandAgent",))


def serialize_aws_json_1_1(value: ManagedAgentName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedAgentName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedAgentName value: {data!r}")
    return cast(ManagedAgentName, data)
