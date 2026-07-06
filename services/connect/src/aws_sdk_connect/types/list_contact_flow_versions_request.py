"""Generated from Smithy shape ``com.amazonaws.connect#ListContactFlowVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result1000
    import aws_sdk_connect.types.next_token


class ListContactFlowVersionsRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    contact_flow_id: "aws_sdk_connect.types.arn.ARN"
    """<p>The identifier of the flow.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of results to return per page. The default MaxResult size is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactFlowVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContactFlowVersionsRequest:
    out: ListContactFlowVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
