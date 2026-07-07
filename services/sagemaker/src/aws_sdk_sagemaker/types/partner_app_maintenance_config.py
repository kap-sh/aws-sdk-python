"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppMaintenanceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.weekly_schedule_time_format


class PartnerAppMaintenanceConfig(TypedDict, closed=True):
    maintenance_window_start: NotRequired[
        "aws_sdk_sagemaker.types.weekly_schedule_time_format.WeeklyScheduleTimeFormat"
    ]
    """<p>The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. This value must take the following format: <code>3-letter-day:24-h-hour:minute</code>. For example: <code>TUE:03:30</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppMaintenanceConfig) -> dict:
    out: dict = {}
    if "maintenance_window_start" in value:
        out["MaintenanceWindowStart"] = value["maintenance_window_start"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerAppMaintenanceConfig:
    out: PartnerAppMaintenanceConfig = {}  # type: ignore[typeddict-item]
    if "MaintenanceWindowStart" in data:
        out["maintenance_window_start"] = data["MaintenanceWindowStart"]
    return out
