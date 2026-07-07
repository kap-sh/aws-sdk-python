"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_version_summaries
    import aws_sdk_bedrock_agent.types.next_token


class ListAgentVersionsResponse(TypedDict, closed=True):
    agent_version_summaries: (
        "aws_sdk_bedrock_agent.types.agent_version_summaries.AgentVersionSummaries"
    )
    """<p>A list of objects, each of which contains information about a version of the agent.</p>"""
    next_token: NotRequired["aws_sdk_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_version_summaries

    out["agentVersionSummaries"] = (
        aws_sdk_bedrock_agent.types.agent_version_summaries.serialize_json(
            value["agent_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentVersionsResponse:
    out: ListAgentVersionsResponse = {}  # type: ignore[typeddict-item]
    if "agentVersionSummaries" in data:
        import aws_sdk_bedrock_agent.types.agent_version_summaries

        out["agent_version_summaries"] = (
            aws_sdk_bedrock_agent.types.agent_version_summaries.deserialize_json(
                data["agentVersionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAgentVersionsResponse.agent_version_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
