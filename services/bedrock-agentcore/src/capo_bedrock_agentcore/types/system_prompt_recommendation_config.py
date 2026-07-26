"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SystemPromptRecommendationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_traces_config
    import capo_bedrock_agentcore.types.recommendation_evaluation_config
    import capo_bedrock_agentcore.types.system_prompt_config


class SystemPromptRecommendationConfig(TypedDict, closed=True):
    system_prompt: (
        "capo_bedrock_agentcore.types.system_prompt_config.SystemPromptConfig"
    )
    """<p>The current system prompt to optimize.</p>"""
    agent_traces: "capo_bedrock_agentcore.types.agent_traces_config.AgentTracesConfig"
    """<p>The agent traces to analyze for generating recommendations.</p>"""
    evaluation_config: "capo_bedrock_agentcore.types.recommendation_evaluation_config.RecommendationEvaluationConfig"
    """<p>The evaluation configuration specifying which evaluator to use for assessing recommendation quality.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemPromptRecommendationConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.system_prompt_config

    out["systemPrompt"] = (
        capo_bedrock_agentcore.types.system_prompt_config.serialize_json(
            value["system_prompt"]
        )
    )
    import capo_bedrock_agentcore.types.agent_traces_config

    out["agentTraces"] = (
        capo_bedrock_agentcore.types.agent_traces_config.serialize_json(
            value["agent_traces"]
        )
    )
    import capo_bedrock_agentcore.types.recommendation_evaluation_config

    out["evaluationConfig"] = (
        capo_bedrock_agentcore.types.recommendation_evaluation_config.serialize_json(
            value["evaluation_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> SystemPromptRecommendationConfig:
    out: SystemPromptRecommendationConfig = {}  # type: ignore[typeddict-item]
    if "systemPrompt" in data:
        import capo_bedrock_agentcore.types.system_prompt_config

        out["system_prompt"] = (
            capo_bedrock_agentcore.types.system_prompt_config.deserialize_json(
                data["systemPrompt"]
            )
        )
    else:
        raise DeserializationError(
            "SystemPromptRecommendationConfig.system_prompt required"
        )
    if "agentTraces" in data:
        import capo_bedrock_agentcore.types.agent_traces_config

        out["agent_traces"] = (
            capo_bedrock_agentcore.types.agent_traces_config.deserialize_json(
                data["agentTraces"]
            )
        )
    else:
        raise DeserializationError(
            "SystemPromptRecommendationConfig.agent_traces required"
        )
    if "evaluationConfig" in data:
        import capo_bedrock_agentcore.types.recommendation_evaluation_config

        out["evaluation_config"] = (
            capo_bedrock_agentcore.types.recommendation_evaluation_config.deserialize_json(
                data["evaluationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "SystemPromptRecommendationConfig.evaluation_config required"
        )
    return out
