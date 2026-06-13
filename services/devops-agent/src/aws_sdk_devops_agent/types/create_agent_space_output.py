"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAgentSpaceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space
    import aws_sdk_devops_agent.types.tags


class CreateAgentSpaceOutput(TypedDict):
    agent_space: "aws_sdk_devops_agent.types.agent_space.AgentSpace"
    tags: NotRequired["aws_sdk_devops_agent.types.tags.Tags"]
    """<p>Tags associated with the created AgentSpace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentSpaceOutput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.agent_space

    out["agentSpace"] = aws_sdk_devops_agent.types.agent_space.serialize_json(
        value["agent_space"]
    )
    if "tags" in value:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentSpaceOutput:
    out: CreateAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    if "agentSpace" in data:
        import aws_sdk_devops_agent.types.agent_space

        out["agent_space"] = aws_sdk_devops_agent.types.agent_space.deserialize_json(
            data["agentSpace"]
        )
    else:
        raise DeserializationError("CreateAgentSpaceOutput.agent_space required")
    if "tags" in data:
        import aws_sdk_devops_agent.types.tags

        out["tags"] = aws_sdk_devops_agent.types.tags.deserialize_json(data["tags"])
    return out
