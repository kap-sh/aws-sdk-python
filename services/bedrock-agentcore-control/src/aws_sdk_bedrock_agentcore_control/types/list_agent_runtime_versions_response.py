"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListAgentRuntimeVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtimes
    import aws_sdk_bedrock_agentcore_control.types.next_token


class ListAgentRuntimeVersionsResponse(TypedDict, closed=True):
    agent_runtimes: (
        "aws_sdk_bedrock_agentcore_control.types.agent_runtimes.AgentRuntimes"
    )
    """<p>The list of AgentCore Runtime versions.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>A token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentRuntimeVersionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.agent_runtimes

    out["agentRuntimes"] = (
        aws_sdk_bedrock_agentcore_control.types.agent_runtimes.serialize_json(
            value["agent_runtimes"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentRuntimeVersionsResponse:
    out: ListAgentRuntimeVersionsResponse = {}  # type: ignore[typeddict-item]
    if "agentRuntimes" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtimes

        out["agent_runtimes"] = (
            aws_sdk_bedrock_agentcore_control.types.agent_runtimes.deserialize_json(
                data["agentRuntimes"]
            )
        )
    else:
        raise DeserializationError(
            "ListAgentRuntimeVersionsResponse.agent_runtimes required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
