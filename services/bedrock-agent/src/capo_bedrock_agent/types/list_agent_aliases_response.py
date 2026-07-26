"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ListAgentAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.agent_alias_summaries
    import capo_bedrock_agent.types.next_token


class ListAgentAliasesResponse(TypedDict, closed=True):
    agent_alias_summaries: (
        "capo_bedrock_agent.types.agent_alias_summaries.AgentAliasSummaries"
    )
    """<p>A list of objects, each of which contains information about an alias of the agent.</p>"""
    next_token: NotRequired["capo_bedrock_agent.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentAliasesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.agent_alias_summaries

    out["agentAliasSummaries"] = (
        capo_bedrock_agent.types.agent_alias_summaries.serialize_json(
            value["agent_alias_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentAliasesResponse:
    out: ListAgentAliasesResponse = {}  # type: ignore[typeddict-item]
    if "agentAliasSummaries" in data:
        import capo_bedrock_agent.types.agent_alias_summaries

        out["agent_alias_summaries"] = (
            capo_bedrock_agent.types.agent_alias_summaries.deserialize_json(
                data["agentAliasSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListAgentAliasesResponse.agent_alias_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
