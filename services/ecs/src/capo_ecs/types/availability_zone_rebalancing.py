"""Generated from Smithy shape ``com.amazonaws.ecs#AvailabilityZoneRebalancing``."""

from typing import Literal, TypeAlias, cast

AvailabilityZoneRebalancing: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AvailabilityZoneRebalancing) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityZoneRebalancing:
    return cast(AvailabilityZoneRebalancing, data)
