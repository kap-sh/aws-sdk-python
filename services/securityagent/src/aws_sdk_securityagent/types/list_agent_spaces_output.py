"""Generated from Smithy shape ``com.amazonaws.securityagent#ListAgentSpacesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_summary_list
    import aws_sdk_securityagent.types.next_token


class ListAgentSpacesOutput(TypedDict):
    agent_space_summaries: NotRequired[
        "aws_sdk_securityagent.types.agent_space_summary_list.AgentSpaceSummaryList"
    ]
    """<p>The list of agent space summaries.</p>"""
    next_token: NotRequired["aws_sdk_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentSpacesOutput) -> dict:
    out: dict = {}
    if "agent_space_summaries" in value:
        import aws_sdk_securityagent.types.agent_space_summary_list

        out["agentSpaceSummaries"] = (
            aws_sdk_securityagent.types.agent_space_summary_list.serialize_json(
                value["agent_space_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentSpacesOutput:
    out: ListAgentSpacesOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaceSummaries" in data:
        import aws_sdk_securityagent.types.agent_space_summary_list

        out["agent_space_summaries"] = (
            aws_sdk_securityagent.types.agent_space_summary_list.deserialize_json(
                data["agentSpaceSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
