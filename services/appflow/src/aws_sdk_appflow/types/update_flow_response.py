"""Generated from Smithy shape ``com.amazonaws.appflow#UpdateFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.flow_status


class UpdateFlowResponse(TypedDict, closed=True):
    flow_status: NotRequired["aws_sdk_appflow.types.flow_status.FlowStatus"]
    """<p>Indicates the current status of the flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowResponse) -> dict:
    out: dict = {}
    if "flow_status" in value:
        import aws_sdk_appflow.types.flow_status

        out["flowStatus"] = aws_sdk_appflow.types.flow_status.serialize_json(
            value["flow_status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowResponse:
    out: UpdateFlowResponse = {}  # type: ignore[typeddict-item]
    if "flowStatus" in data:
        import aws_sdk_appflow.types.flow_status

        out["flow_status"] = aws_sdk_appflow.types.flow_status.deserialize_json(
            data["flowStatus"]
        )
    return out
