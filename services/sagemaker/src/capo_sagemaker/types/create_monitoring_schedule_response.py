"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateMonitoringScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_schedule_arn


class CreateMonitoringScheduleResponse(TypedDict, closed=True):
    monitoring_schedule_arn: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_arn.MonitoringScheduleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the monitoring schedule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMonitoringScheduleResponse) -> dict:
    out: dict = {}
    if "monitoring_schedule_arn" in value:
        out["MonitoringScheduleArn"] = value["monitoring_schedule_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMonitoringScheduleResponse:
    out: CreateMonitoringScheduleResponse = {}  # type: ignore[typeddict-item]
    if "MonitoringScheduleArn" in data:
        out["monitoring_schedule_arn"] = data["MonitoringScheduleArn"]
    return out
