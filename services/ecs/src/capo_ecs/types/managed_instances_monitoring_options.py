"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesMonitoringOptions``."""

from typing import Literal, TypeAlias, cast

ManagedInstancesMonitoringOptions: TypeAlias = Literal[
    "BASIC",
    "DETAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedInstancesMonitoringOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedInstancesMonitoringOptions:
    return cast(ManagedInstancesMonitoringOptions, data)
