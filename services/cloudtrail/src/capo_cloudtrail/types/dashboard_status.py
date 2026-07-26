"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DashboardStatus``."""

from typing import Literal, TypeAlias, cast

DashboardStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "UPDATING",
    "UPDATED",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DashboardStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DashboardStatus:
    return cast(DashboardStatus, data)
