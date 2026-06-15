"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedDescriptorsUnion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.updated_a2a_descriptor
    import aws_sdk_bedrock_agentcore_control.types.updated_agent_skills_descriptor
    import aws_sdk_bedrock_agentcore_control.types.updated_custom_descriptor
    import aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor


class UpdatedDescriptorsUnion(TypedDict):
    mcp: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor.UpdatedMcpDescriptor"
    ]
    """<p>The updated MCP descriptor.</p>"""
    a2a: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.updated_a2a_descriptor.UpdatedA2aDescriptor"
    ]
    """<p>The updated A2A descriptor.</p>"""
    custom: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.updated_custom_descriptor.UpdatedCustomDescriptor"
    ]
    """<p>The updated custom descriptor.</p>"""
    agent_skills: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.updated_agent_skills_descriptor.UpdatedAgentSkillsDescriptor"
    ]
    """<p>The updated agent skills descriptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedDescriptorsUnion) -> dict:
    out: dict = {}
    if "mcp" in value:
        import aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor

        out["mcp"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor.serialize_json(
                value["mcp"]
            )
        )
    if "a2a" in value:
        import aws_sdk_bedrock_agentcore_control.types.updated_a2a_descriptor

        out["a2a"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_a2a_descriptor.serialize_json(
                value["a2a"]
            )
        )
    if "custom" in value:
        import aws_sdk_bedrock_agentcore_control.types.updated_custom_descriptor

        out["custom"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_custom_descriptor.serialize_json(
                value["custom"]
            )
        )
    if "agent_skills" in value:
        import aws_sdk_bedrock_agentcore_control.types.updated_agent_skills_descriptor

        out["agentSkills"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_agent_skills_descriptor.serialize_json(
                value["agent_skills"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedDescriptorsUnion:
    out: UpdatedDescriptorsUnion = {}  # type: ignore[typeddict-item]
    if "mcp" in data:
        import aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor

        out["mcp"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_mcp_descriptor.deserialize_json(
                data["mcp"]
            )
        )
    if "a2a" in data:
        import aws_sdk_bedrock_agentcore_control.types.updated_a2a_descriptor

        out["a2a"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_a2a_descriptor.deserialize_json(
                data["a2a"]
            )
        )
    if "custom" in data:
        import aws_sdk_bedrock_agentcore_control.types.updated_custom_descriptor

        out["custom"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_custom_descriptor.deserialize_json(
                data["custom"]
            )
        )
    if "agentSkills" in data:
        import aws_sdk_bedrock_agentcore_control.types.updated_agent_skills_descriptor

        out["agent_skills"] = (
            aws_sdk_bedrock_agentcore_control.types.updated_agent_skills_descriptor.deserialize_json(
                data["agentSkills"]
            )
        )
    return out
