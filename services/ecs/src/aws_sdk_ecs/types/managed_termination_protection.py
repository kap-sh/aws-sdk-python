"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTerminationProtection``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ManagedTerminationProtection: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ManagedTerminationProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedTerminationProtection:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ManagedTerminationProtection value: {data!r}"
        )
    return cast(ManagedTerminationProtection, data)
