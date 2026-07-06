"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.flow_id
    import aws_sdk_quicksight.types.status_code


class UpdateFlowResponse(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    flow_id: "aws_sdk_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateFlowResponse:
    out: UpdateFlowResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateFlowResponse.arn required")
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    else:
        raise DeserializationError("UpdateFlowResponse.flow_id required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
