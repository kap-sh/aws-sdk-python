"""Generated from Smithy shape ``com.amazonaws.ecs#PidMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

PidMode: TypeAlias = Literal[
    "host",
    "task",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "host",
        "task",
    )
)


def serialize_aws_json_1_1(value: PidMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PidMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PidMode value: {data!r}")
    return cast(PidMode, data)
