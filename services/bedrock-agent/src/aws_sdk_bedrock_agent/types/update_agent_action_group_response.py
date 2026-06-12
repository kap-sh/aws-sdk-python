"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateAgentActionGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_action_group


class UpdateAgentActionGroupResponse(TypedDict):
    agent_action_group: (
        "aws_sdk_bedrock_agent.types.agent_action_group.AgentActionGroup"
    )
    """<p>Contains details about the action group that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentActionGroupResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.agent_action_group

    out["agentActionGroup"] = (
        aws_sdk_bedrock_agent.types.agent_action_group.serialize_json(
            value["agent_action_group"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentActionGroupResponse:
    out: UpdateAgentActionGroupResponse = {}  # type: ignore[typeddict-item]
    if "agentActionGroup" in data:
        import aws_sdk_bedrock_agent.types.agent_action_group

        out["agent_action_group"] = (
            aws_sdk_bedrock_agent.types.agent_action_group.deserialize_json(
                data["agentActionGroup"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentActionGroupResponse.agent_action_group required"
        )
    return out
