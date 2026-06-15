"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionRecommendationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.agent_traces_config
    import aws_sdk_bedrock_agentcore.types.tool_description_source


class ToolDescriptionRecommendationConfig(TypedDict):
    tool_description: (
        "aws_sdk_bedrock_agentcore.types.tool_description_source.ToolDescriptionSource"
    )
    """<p>The current tool descriptions to optimize.</p>"""
    agent_traces: (
        "aws_sdk_bedrock_agentcore.types.agent_traces_config.AgentTracesConfig"
    )
    """<p>The agent traces to analyze for generating tool description recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionRecommendationConfig) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.tool_description_source

    out["toolDescription"] = (
        aws_sdk_bedrock_agentcore.types.tool_description_source.serialize_json(
            value["tool_description"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.agent_traces_config

    out["agentTraces"] = (
        aws_sdk_bedrock_agentcore.types.agent_traces_config.serialize_json(
            value["agent_traces"]
        )
    )
    return out


def deserialize_json(data: dict) -> ToolDescriptionRecommendationConfig:
    out: ToolDescriptionRecommendationConfig = {}  # type: ignore[typeddict-item]
    if "toolDescription" in data:
        import aws_sdk_bedrock_agentcore.types.tool_description_source

        out["tool_description"] = (
            aws_sdk_bedrock_agentcore.types.tool_description_source.deserialize_json(
                data["toolDescription"]
            )
        )
    else:
        raise DeserializationError(
            "ToolDescriptionRecommendationConfig.tool_description required"
        )
    if "agentTraces" in data:
        import aws_sdk_bedrock_agentcore.types.agent_traces_config

        out["agent_traces"] = (
            aws_sdk_bedrock_agentcore.types.agent_traces_config.deserialize_json(
                data["agentTraces"]
            )
        )
    else:
        raise DeserializationError(
            "ToolDescriptionRecommendationConfig.agent_traces required"
        )
    return out
