"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListFlowVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_version_summaries
    import aws_sdk_bedrock_agent.types.next_token


class ListFlowVersionsResponse(TypedDict):
    flow_version_summaries: (
        "aws_sdk_bedrock_agent.types.flow_version_summaries.FlowVersionSummaries"
    )
    """<p>A list, each member of which contains information about a flow.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFlowVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.flow_version_summaries

    out["flowVersionSummaries"] = (
        aws_sdk_bedrock_agent.types.flow_version_summaries.serialize_json(
            value["flow_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFlowVersionsResponse:
    out: ListFlowVersionsResponse = {}  # type: ignore[typeddict-item]
    if "flowVersionSummaries" in data:
        import aws_sdk_bedrock_agent.types.flow_version_summaries

        out["flow_version_summaries"] = (
            aws_sdk_bedrock_agent.types.flow_version_summaries.deserialize_json(
                data["flowVersionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListFlowVersionsResponse.flow_version_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
