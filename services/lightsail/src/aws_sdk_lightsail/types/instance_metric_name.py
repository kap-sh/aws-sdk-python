"""Generated from Smithy shape ``com.amazonaws.lightsail#InstanceMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

InstanceMetricName: TypeAlias = Literal[
    "CPUUtilization",
    "NetworkIn",
    "NetworkOut",
    "StatusCheckFailed",
    "StatusCheckFailed_Instance",
    "StatusCheckFailed_System",
    "BurstCapacityTime",
    "BurstCapacityPercentage",
    "MetadataNoToken",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPUUtilization",
        "NetworkIn",
        "NetworkOut",
        "StatusCheckFailed",
        "StatusCheckFailed_Instance",
        "StatusCheckFailed_System",
        "BurstCapacityTime",
        "BurstCapacityPercentage",
        "MetadataNoToken",
    )
)


def serialize_aws_json_1_1(value: InstanceMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InstanceMetricName value: {data!r}")
    return cast(InstanceMetricName, data)
