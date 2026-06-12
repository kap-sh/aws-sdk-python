"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateAnomalyMonitorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class UpdateAnomalyMonitorResponse(TypedDict):
    monitor_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>A cost anomaly monitor ARN. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAnomalyMonitorResponse) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAnomalyMonitorResponse:
    out: UpdateAnomalyMonitorResponse = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("UpdateAnomalyMonitorResponse.monitor_arn required")
    return out
