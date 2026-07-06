"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#ListFlowExecutionMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.flow_execution_id
    import aws_sdk_iotthingsgraph.types.max_results
    import aws_sdk_iotthingsgraph.types.next_token


class ListFlowExecutionMessagesRequest(TypedDict, closed=True):
    flow_execution_id: "aws_sdk_iotthingsgraph.types.flow_execution_id.FlowExecutionId"
    """<p>The ID of the flow execution.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results. Use this when you're paginating results.</p>"""
    max_results: NotRequired["aws_sdk_iotthingsgraph.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFlowExecutionMessagesRequest) -> dict:
    out: dict = {}
    out["flowExecutionId"] = value["flow_execution_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFlowExecutionMessagesRequest:
    out: ListFlowExecutionMessagesRequest = {}  # type: ignore[typeddict-item]
    if "flowExecutionId" in data:
        out["flow_execution_id"] = data["flowExecutionId"]
    else:
        raise DeserializationError(
            "ListFlowExecutionMessagesRequest.flow_execution_id required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
