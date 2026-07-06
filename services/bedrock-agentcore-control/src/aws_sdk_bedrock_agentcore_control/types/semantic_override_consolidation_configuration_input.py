"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SemanticOverrideConsolidationConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.prompt


class SemanticOverrideConsolidationConfigurationInput(TypedDict, closed=True):
    append_to_prompt: "aws_sdk_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for semantic consolidation.</p>"""
    model_id: "str"
    """<p>The model ID to use for semantic consolidation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticOverrideConsolidationConfigurationInput) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> SemanticOverrideConsolidationConfigurationInput:
    out: SemanticOverrideConsolidationConfigurationInput = {}  # type: ignore[typeddict-item]
    if "appendToPrompt" in data:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "SemanticOverrideConsolidationConfigurationInput.append_to_prompt required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "SemanticOverrideConsolidationConfigurationInput.model_id required"
        )
    return out
