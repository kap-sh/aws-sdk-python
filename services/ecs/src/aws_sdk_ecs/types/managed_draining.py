"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedDraining``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

ManagedDraining: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ManagedDraining) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedDraining:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedDraining value: {data!r}")
    return cast(ManagedDraining, data)
