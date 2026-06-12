"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeFlowExecutionRecordsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.flow_name
    import aws_sdk_appflow.types.max_results
    import aws_sdk_appflow.types.next_token


class DescribeFlowExecutionRecordsRequest(TypedDict):
    flow_name: "aws_sdk_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""
    max_results: NotRequired["aws_sdk_appflow.types.max_results.MaxResults"]
    """<p> Specifies the maximum number of items that should be returned in the result set. The default for <code>maxResults</code> is 20 (for all paginated API operations). </p>"""
    next_token: NotRequired["aws_sdk_appflow.types.next_token.NextToken"]
    """<p> The pagination token for the next page of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowExecutionRecordsRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeFlowExecutionRecordsRequest:
    out: DescribeFlowExecutionRecordsRequest = {}  # type: ignore[typeddict-item]
    if "flowName" in data:
        out["flow_name"] = data["flowName"]
    else:
        raise DeserializationError(
            "DescribeFlowExecutionRecordsRequest.flow_name required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
