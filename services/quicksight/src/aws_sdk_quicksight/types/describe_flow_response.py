"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.flow_detail
    import aws_sdk_quicksight.types.status_code


class DescribeFlowResponse(TypedDict, closed=True):
    flow: "aws_sdk_quicksight.types.flow_detail.FlowDetail"
    """<p>The full details of the flow.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowResponse) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.flow_detail

    out["Flow"] = aws_sdk_quicksight.types.flow_detail.serialize_json(value["flow"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeFlowResponse:
    out: DescribeFlowResponse = {}  # type: ignore[typeddict-item]
    if "Flow" in data:
        import aws_sdk_quicksight.types.flow_detail

        out["flow"] = aws_sdk_quicksight.types.flow_detail.deserialize_json(
            data["Flow"]
        )
    else:
        raise DeserializationError("DescribeFlowResponse.flow required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
