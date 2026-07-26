"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EpisodicOverrideExtractionConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.prompt


class EpisodicOverrideExtractionConfigurationInput(TypedDict, closed=True):
    append_to_prompt: "capo_bedrock_agentcore_control.types.prompt.Prompt"
    """<p>The text to append to the prompt for the extraction step of the episodic memory strategy.</p>"""
    model_id: "str"
    """<p>The model ID to use for the extraction step of the episodic memory strategy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EpisodicOverrideExtractionConfigurationInput) -> dict:
    out: dict = {}
    out["appendToPrompt"] = value["append_to_prompt"]
    out["modelId"] = value["model_id"]
    return out


def deserialize_json(data: dict) -> EpisodicOverrideExtractionConfigurationInput:
    out: EpisodicOverrideExtractionConfigurationInput = {}  # type: ignore[typeddict-item]
    if "appendToPrompt" in data:
        out["append_to_prompt"] = data["appendToPrompt"]
    else:
        raise DeserializationError(
            "EpisodicOverrideExtractionConfigurationInput.append_to_prompt required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "EpisodicOverrideExtractionConfigurationInput.model_id required"
        )
    return out
