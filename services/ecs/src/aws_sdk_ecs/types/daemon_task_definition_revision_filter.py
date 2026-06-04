"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionRevisionFilter``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

DaemonTaskDefinitionRevisionFilter: TypeAlias = Literal["LAST_REGISTERED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LAST_REGISTERED",))


def serialize_aws_json_1_1(value: DaemonTaskDefinitionRevisionFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonTaskDefinitionRevisionFilter:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DaemonTaskDefinitionRevisionFilter value: {data!r}"
        )
    return cast(DaemonTaskDefinitionRevisionFilter, data)
