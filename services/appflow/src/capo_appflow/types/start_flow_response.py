"""Generated from Smithy shape ``com.amazonaws.appflow#StartFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.execution_id
    import capo_appflow.types.flow_arn
    import capo_appflow.types.flow_status


class StartFlowResponse(TypedDict, closed=True):
    flow_arn: NotRequired["capo_appflow.types.flow_arn.FlowArn"]
    """<p> The flow's Amazon Resource Name (ARN). </p>"""
    flow_status: NotRequired["capo_appflow.types.flow_status.FlowStatus"]
    """<p> Indicates the current status of the flow. </p>"""
    execution_id: NotRequired["capo_appflow.types.execution_id.ExecutionId"]
    """<p> Returns the internal execution ID of an on-demand flow when the flow is started. For scheduled or event-triggered flows, this value is null. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_status" in value:
        import capo_appflow.types.flow_status

        out["flowStatus"] = capo_appflow.types.flow_status.serialize_json(
            value["flow_status"]
        )
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> StartFlowResponse:
    out: StartFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowStatus" in data:
        import capo_appflow.types.flow_status

        out["flow_status"] = capo_appflow.types.flow_status.deserialize_json(
            data["flowStatus"]
        )
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    return out
