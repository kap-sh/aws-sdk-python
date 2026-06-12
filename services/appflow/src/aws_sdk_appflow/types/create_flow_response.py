"""Generated from Smithy shape ``com.amazonaws.appflow#CreateFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.flow_arn
    import aws_sdk_appflow.types.flow_status


class CreateFlowResponse(TypedDict):
    flow_arn: NotRequired["aws_sdk_appflow.types.flow_arn.FlowArn"]
    """<p> The flow's Amazon Resource Name (ARN). </p>"""
    flow_status: NotRequired["aws_sdk_appflow.types.flow_status.FlowStatus"]
    """<p> Indicates the current status of the flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_status" in value:
        import aws_sdk_appflow.types.flow_status

        out["flowStatus"] = aws_sdk_appflow.types.flow_status.serialize_json(
            value["flow_status"]
        )
    return out


def deserialize_json(data: dict) -> CreateFlowResponse:
    out: CreateFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowStatus" in data:
        import aws_sdk_appflow.types.flow_status

        out["flow_status"] = aws_sdk_appflow.types.flow_status.deserialize_json(
            data["flowStatus"]
        )
    return out
