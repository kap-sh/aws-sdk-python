"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAgentSpaceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space


class UpdateAgentSpaceOutput(TypedDict, closed=True):
    agent_space: "aws_sdk_devops_agent.types.agent_space.AgentSpace"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentSpaceOutput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.agent_space

    out["agentSpace"] = aws_sdk_devops_agent.types.agent_space.serialize_json(
        value["agent_space"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentSpaceOutput:
    out: UpdateAgentSpaceOutput = {}  # type: ignore[typeddict-item]
    if "agentSpace" in data:
        import aws_sdk_devops_agent.types.agent_space

        out["agent_space"] = aws_sdk_devops_agent.types.agent_space.deserialize_json(
            data["agentSpace"]
        )
    else:
        raise DeserializationError("UpdateAgentSpaceOutput.agent_space required")
    return out
