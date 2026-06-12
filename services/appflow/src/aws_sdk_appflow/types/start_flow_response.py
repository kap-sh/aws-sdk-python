"""Generated from Smithy shape ``com.amazonaws.appflow#StartFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.execution_id
    import aws_sdk_appflow.types.flow_arn
    import aws_sdk_appflow.types.flow_status


class StartFlowResponse(TypedDict):
    flow_arn: NotRequired["aws_sdk_appflow.types.flow_arn.FlowArn"]
    """<p> The flow's Amazon Resource Name (ARN). </p>"""
    flow_status: NotRequired["aws_sdk_appflow.types.flow_status.FlowStatus"]
    """<p> Indicates the current status of the flow. </p>"""
    execution_id: NotRequired["aws_sdk_appflow.types.execution_id.ExecutionId"]
    """<p> Returns the internal execution ID of an on-demand flow when the flow is started. For scheduled or event-triggered flows, this value is null. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_status" in value:
        import aws_sdk_appflow.types.flow_status

        out["flowStatus"] = aws_sdk_appflow.types.flow_status.serialize_json(
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
        import aws_sdk_appflow.types.flow_status

        out["flow_status"] = aws_sdk_appflow.types.flow_status.deserialize_json(
            data["flowStatus"]
        )
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    return out
