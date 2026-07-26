"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopMonitoringScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_schedule_name


class StopMonitoringScheduleRequest(TypedDict, closed=True):
    monitoring_schedule_name: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of the schedule to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopMonitoringScheduleRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopMonitoringScheduleRequest:
    out: StopMonitoringScheduleRequest = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleName" in data:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    return out
