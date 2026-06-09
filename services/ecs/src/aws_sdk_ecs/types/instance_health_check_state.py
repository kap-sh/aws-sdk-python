"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

InstanceHealthCheckState: TypeAlias = Literal[
    "OK",
    "IMPAIRED",
    "INSUFFICIENT_DATA",
    "INITIALIZING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "IMPAIRED",
        "INSUFFICIENT_DATA",
        "INITIALIZING",
    )
)


def serialize_aws_json_1_1(value: InstanceHealthCheckState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthCheckState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceHealthCheckState value: {data!r}")
    return cast(InstanceHealthCheckState, data)
