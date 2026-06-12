"""Generated from Smithy shape ``com.amazonaws.costexplorer#DeleteAnomalyMonitorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class DeleteAnomalyMonitorRequest(TypedDict):
    monitor_arn: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The unique identifier of the cost anomaly monitor that you want to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAnomalyMonitorRequest) -> dict:
    out: dict = {}
    out["MonitorArn"] = value["monitor_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAnomalyMonitorRequest:
    out: DeleteAnomalyMonitorRequest = {}  # type: ignore[typeddict-item]
    if "MonitorArn" in data:
        out["monitor_arn"] = data["MonitorArn"]
    else:
        raise DeserializationError("DeleteAnomalyMonitorRequest.monitor_arn required")
    return out
