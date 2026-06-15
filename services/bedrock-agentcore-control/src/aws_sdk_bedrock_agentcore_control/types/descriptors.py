"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Descriptors``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.a2a_descriptor
    import aws_sdk_bedrock_agentcore_control.types.agent_skills_descriptor
    import aws_sdk_bedrock_agentcore_control.types.custom_descriptor
    import aws_sdk_bedrock_agentcore_control.types.mcp_descriptor


class Descriptors(TypedDict):
    mcp: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.mcp_descriptor.McpDescriptor"
    ]
    """<p>The Model Context Protocol (MCP) descriptor configuration. Use this when the <code>descriptorType</code> is <code>MCP</code>.</p>"""
    a2a: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.a2a_descriptor.A2aDescriptor"
    ]
    """<p>The Agent-to-Agent (A2A) protocol descriptor configuration. Use this when the <code>descriptorType</code> is <code>A2A</code>.</p>"""
    custom: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.custom_descriptor.CustomDescriptor"
    ]
    """<p>The custom descriptor configuration. Use this when the <code>descriptorType</code> is <code>CUSTOM</code>.</p>"""
    agent_skills: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.agent_skills_descriptor.AgentSkillsDescriptor"
    ]
    """<p>The agent skills descriptor configuration. Use this when the <code>descriptorType</code> is <code>AGENT_SKILLS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Descriptors) -> dict:
    out: dict = {}
    if "mcp" in value:
        import aws_sdk_bedrock_agentcore_control.types.mcp_descriptor

        out["mcp"] = (
            aws_sdk_bedrock_agentcore_control.types.mcp_descriptor.serialize_json(
                value["mcp"]
            )
        )
    if "a2a" in value:
        import aws_sdk_bedrock_agentcore_control.types.a2a_descriptor

        out["a2a"] = (
            aws_sdk_bedrock_agentcore_control.types.a2a_descriptor.serialize_json(
                value["a2a"]
            )
        )
    if "custom" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_descriptor

        out["custom"] = (
            aws_sdk_bedrock_agentcore_control.types.custom_descriptor.serialize_json(
                value["custom"]
            )
        )
    if "agent_skills" in value:
        import aws_sdk_bedrock_agentcore_control.types.agent_skills_descriptor

        out["agentSkills"] = (
            aws_sdk_bedrock_agentcore_control.types.agent_skills_descriptor.serialize_json(
                value["agent_skills"]
            )
        )
    return out


def deserialize_json(data: dict) -> Descriptors:
    out: Descriptors = {}  # type: ignore[typeddict-item]
    if "mcp" in data:
        import aws_sdk_bedrock_agentcore_control.types.mcp_descriptor

        out["mcp"] = (
            aws_sdk_bedrock_agentcore_control.types.mcp_descriptor.deserialize_json(
                data["mcp"]
            )
        )
    if "a2a" in data:
        import aws_sdk_bedrock_agentcore_control.types.a2a_descriptor

        out["a2a"] = (
            aws_sdk_bedrock_agentcore_control.types.a2a_descriptor.deserialize_json(
                data["a2a"]
            )
        )
    if "custom" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_descriptor

        out["custom"] = (
            aws_sdk_bedrock_agentcore_control.types.custom_descriptor.deserialize_json(
                data["custom"]
            )
        )
    if "agentSkills" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_skills_descriptor

        out["agent_skills"] = (
            aws_sdk_bedrock_agentcore_control.types.agent_skills_descriptor.deserialize_json(
                data["agentSkills"]
            )
        )
    return out
