"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandLogging``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ExecuteCommandLogging: TypeAlias = Literal[
    "NONE",
    "DEFAULT",
    "OVERRIDE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DEFAULT",
        "OVERRIDE",
    )
)


def serialize_aws_json_1_1(value: ExecuteCommandLogging) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecuteCommandLogging:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecuteCommandLogging value: {data!r}")
    return cast(ExecuteCommandLogging, data)
