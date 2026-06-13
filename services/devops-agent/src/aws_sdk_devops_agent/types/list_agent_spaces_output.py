"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAgentSpacesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_list
    import aws_sdk_devops_agent.types.next_token


class ListAgentSpacesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Token to retrieve the next page of results, if there are more results.</p>"""
    agent_spaces: "aws_sdk_devops_agent.types.agent_space_list.AgentSpaceList"
    """<p>The list of AgentSpaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentSpacesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_devops_agent.types.agent_space_list

    out["agentSpaces"] = aws_sdk_devops_agent.types.agent_space_list.serialize_json(
        value["agent_spaces"]
    )
    return out


def deserialize_json(data: dict) -> ListAgentSpacesOutput:
    out: ListAgentSpacesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "agentSpaces" in data:
        import aws_sdk_devops_agent.types.agent_space_list

        out["agent_spaces"] = (
            aws_sdk_devops_agent.types.agent_space_list.deserialize_json(
                data["agentSpaces"]
            )
        )
    else:
        raise DeserializationError("ListAgentSpacesOutput.agent_spaces required")
    return out
