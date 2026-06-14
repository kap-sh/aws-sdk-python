"""Generated from Smithy shape ``com.amazonaws.workspaces#RunningMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

RunningMode: TypeAlias = Literal[
    "AUTO_STOP",
    "ALWAYS_ON",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_STOP",
        "ALWAYS_ON",
        "MANUAL",
    )
)


def serialize_aws_json_1_1(value: RunningMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RunningMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RunningMode value: {data!r}")
    return cast(RunningMode, data)
