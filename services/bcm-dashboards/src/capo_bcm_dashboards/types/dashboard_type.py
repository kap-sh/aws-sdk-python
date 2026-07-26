"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DashboardType``."""

from typing import Literal, TypeAlias, cast

DashboardType: TypeAlias = Literal["CUSTOM",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DashboardType:
    return cast(DashboardType, data)
