"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileCacheLustreConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.weekly_time


class UpdateFileCacheLustreConfiguration(TypedDict):
    weekly_maintenance_start_time: NotRequired[
        "aws_sdk_fsx.types.weekly_time.WeeklyTime"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileCacheLustreConfiguration) -> dict:
    out: dict = {}
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileCacheLustreConfiguration:
    out: UpdateFileCacheLustreConfiguration = {}  # type: ignore[typeddict-item]
    if "WeeklyMaintenanceStartTime" in data:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    return out
