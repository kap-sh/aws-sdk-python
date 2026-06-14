"""Generated from Smithy shape ``com.amazonaws.workspaces#PoolsRunningMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

PoolsRunningMode: TypeAlias = Literal[
    "AUTO_STOP",
    "ALWAYS_ON",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_STOP",
        "ALWAYS_ON",
    )
)


def serialize_aws_json_1_1(value: PoolsRunningMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PoolsRunningMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PoolsRunningMode value: {data!r}")
    return cast(PoolsRunningMode, data)
