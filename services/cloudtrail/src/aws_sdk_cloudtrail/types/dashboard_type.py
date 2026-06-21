"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DashboardType``."""

from typing import Literal, TypeAlias, cast

DashboardType: TypeAlias = Literal[
    "MANAGED",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DashboardType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DashboardType:
    return cast(DashboardType, data)
