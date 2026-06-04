"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesMonitoringOptions``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ManagedInstancesMonitoringOptions: TypeAlias = Literal[
    "BASIC",
    "DETAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "DETAILED",
    )
)


def serialize_aws_json_1_1(value: ManagedInstancesMonitoringOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedInstancesMonitoringOptions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ManagedInstancesMonitoringOptions value: {data!r}"
        )
    return cast(ManagedInstancesMonitoringOptions, data)
