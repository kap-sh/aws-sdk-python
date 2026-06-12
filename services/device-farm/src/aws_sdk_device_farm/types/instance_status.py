"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

InstanceStatus: TypeAlias = Literal[
    "IN_USE",
    "PREPARING",
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_USE",
        "PREPARING",
        "AVAILABLE",
        "NOT_AVAILABLE",
    )
)


def serialize_aws_json_1_1(value: InstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceStatus value: {data!r}")
    return cast(InstanceStatus, data)
