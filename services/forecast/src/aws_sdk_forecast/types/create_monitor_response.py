"""Generated from Smithy shape ``com.amazonaws.forecast#CreateMonitorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class CreateMonitorResponse(TypedDict, closed=True):
    monitor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the monitor resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMonitorResponse) -> dict:
    out: dict = {}
    if "monitor_arn" in value:
        out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMonitorResponse:
    out: CreateMonitorResponse = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    return out
