"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgentActionGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_action_group

AgentActionGroups: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.agent_action_group.AgentActionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AgentActionGroups) -> list:
    import aws_sdk_bedrock_agent_runtime.types.agent_action_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.agent_action_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AgentActionGroups:
    import aws_sdk_bedrock_agent_runtime.types.agent_action_group

    out: AgentActionGroups = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.agent_action_group.deserialize_json(
                item
            )
        )
    return out
