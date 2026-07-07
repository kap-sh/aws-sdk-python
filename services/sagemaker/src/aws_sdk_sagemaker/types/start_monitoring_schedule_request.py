"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartMonitoringScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_schedule_name


class StartMonitoringScheduleRequest(TypedDict, closed=True):
    monitoring_schedule_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of the schedule to start.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMonitoringScheduleRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMonitoringScheduleRequest:
    out: StartMonitoringScheduleRequest = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    return out
