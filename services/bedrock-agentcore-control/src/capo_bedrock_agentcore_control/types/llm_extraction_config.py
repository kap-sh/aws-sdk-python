"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LlmExtractionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.definition
    import capo_bedrock_agentcore_control.types.llm_extraction_instruction
    import capo_bedrock_agentcore_control.types.validation


class LlmExtractionConfig(TypedDict, closed=True):
    llm_extraction_instruction: NotRequired[
        "capo_bedrock_agentcore_control.types.llm_extraction_instruction.LlmExtractionInstruction"
    ]
    """<p>Instructions for extraction. Supports built-in operators like LATEST_VALUE or custom natural-language instructions.</p>"""
    definition: "capo_bedrock_agentcore_control.types.definition.Definition"
    """<p>Description of what this metadata field represents.</p>"""
    validation: NotRequired[
        "capo_bedrock_agentcore_control.types.validation.Validation"
    ]
    """<p>Validation rules to constrain extracted values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LlmExtractionConfig) -> dict:
    out: dict = {}
    if "llm_extraction_instruction" in value:
        out["llmExtractionInstruction"] = value["llm_extraction_instruction"]
    out["definition"] = value["definition"]
    if "validation" in value:
        import capo_bedrock_agentcore_control.types.validation

        out["validation"] = (
            capo_bedrock_agentcore_control.types.validation.serialize_json(
                value["validation"]
            )
        )
    return out


def deserialize_json(data: dict) -> LlmExtractionConfig:
    out: LlmExtractionConfig = {}  # type: ignore[typeddict-item]
    if "llmExtractionInstruction" in data:
        out["llm_extraction_instruction"] = data["llmExtractionInstruction"]
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("LlmExtractionConfig.definition required")
    if "validation" in data:
        import capo_bedrock_agentcore_control.types.validation

        out["validation"] = (
            capo_bedrock_agentcore_control.types.validation.deserialize_json(
                data["validation"]
            )
        )
    return out
