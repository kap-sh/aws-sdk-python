"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContainerServiceMetricName: TypeAlias = Literal[
    "CPUUtilization",
    "MemoryUtilization",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPUUtilization",
        "MemoryUtilization",
    )
)


def serialize_aws_json_1_1(value: ContainerServiceMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceMetricName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContainerServiceMetricName value: {data!r}"
        )
    return cast(ContainerServiceMetricName, data)
