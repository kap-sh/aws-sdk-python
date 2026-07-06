"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_summaries
    import aws_sdk_bedrock_agent.types.next_token


class ListAgentsResponse(TypedDict, closed=True):
    agent_summaries: "aws_sdk_bedrock_agent.types.agent_summaries.AgentSummaries"
    """<p>A list of objects, each of which contains information about an agent.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_summaries

    out["agentSummaries"] = aws_sdk_bedrock_agent.types.agent_summaries.serialize_json(
        value["agent_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentsResponse:
    out: ListAgentsResponse = {}  # type: ignore[typeddict-item]
    if "agentSummaries" in data:
        import aws_sdk_bedrock_agent.types.agent_summaries

        out["agent_summaries"] = (
            aws_sdk_bedrock_agent.types.agent_summaries.deserialize_json(
                data["agentSummaries"]
            )
        )
    else:
        raise DeserializationError("ListAgentsResponse.agent_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
