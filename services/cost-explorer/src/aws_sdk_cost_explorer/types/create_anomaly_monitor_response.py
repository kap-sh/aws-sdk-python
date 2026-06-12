"""Generated from Smithy shape ``com.amazonaws.costexplorer#CreateAnomalyMonitorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class CreateAnomalyMonitorResponse(TypedDict):
    monitor_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of your newly created cost anomaly detection monitor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAnomalyMonitorResponse) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAnomalyMonitorResponse:
    out: CreateAnomalyMonitorResponse = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("CreateAnomalyMonitorResponse.monitor_arn required")
    return out
