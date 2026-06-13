"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListFlowExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_summaries
    import aws_sdk_bedrock_agent_runtime.types.next_token


class ListFlowExecutionsResponse(TypedDict):
    flow_execution_summaries: "aws_sdk_bedrock_agent_runtime.types.flow_execution_summaries.FlowExecutionSummaries"
    """<p>A list of flow execution summaries. Each summary includes the execution ARN, flow identifier, flow alias identifier, flow version, status, and timestamps.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This value is returned if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowExecutionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.flow_execution_summaries

    out["flowExecutionSummaries"] = (
        aws_sdk_bedrock_agent_runtime.types.flow_execution_summaries.serialize_json(
            value["flow_execution_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowExecutionsResponse:
    out: ListFlowExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "flowExecutionSummaries" in data:
        import aws_sdk_bedrock_agent_runtime.types.flow_execution_summaries

        out["flow_execution_summaries"] = (
            aws_sdk_bedrock_agent_runtime.types.flow_execution_summaries.deserialize_json(
                data["flowExecutionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListFlowExecutionsResponse.flow_execution_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
