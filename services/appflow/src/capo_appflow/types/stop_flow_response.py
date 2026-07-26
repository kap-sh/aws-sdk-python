"""Generated from Smithy shape ``com.amazonaws.appflow#StopFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.flow_arn
    import capo_appflow.types.flow_status


class StopFlowResponse(TypedDict, closed=True):
    flow_arn: NotRequired["capo_appflow.types.flow_arn.FlowArn"]
    """<p> The flow's Amazon Resource Name (ARN). </p>"""
    flow_status: NotRequired["capo_appflow.types.flow_status.FlowStatus"]
    """<p> Indicates the current status of the flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopFlowResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "flow_status" in value:
        import capo_appflow.types.flow_status

        out["flowStatus"] = capo_appflow.types.flow_status.serialize_json(
            value["flow_status"]
        )
    return out


def deserialize_json(data: dict) -> StopFlowResponse:
    out: StopFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "flowStatus" in data:
        import capo_appflow.types.flow_status

        out["flow_status"] = capo_appflow.types.flow_status.deserialize_json(
            data["flowStatus"]
        )
    return out
