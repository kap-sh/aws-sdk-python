"""Generated from Smithy shape ``com.amazonaws.ecs#AvailabilityZoneRebalancing``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

AvailabilityZoneRebalancing: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AvailabilityZoneRebalancing) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityZoneRebalancing:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AvailabilityZoneRebalancing value: {data!r}"
        )
    return cast(AvailabilityZoneRebalancing, data)
