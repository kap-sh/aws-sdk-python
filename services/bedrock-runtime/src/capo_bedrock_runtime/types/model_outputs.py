"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ModelOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_output_text

ModelOutputs: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_output_text.GuardrailOutputText"
]


# --- restJson1 ser/de ---
def serialize_json(value: ModelOutputs) -> list:
    return list(value)


def deserialize_json(data: list) -> ModelOutputs:
    return [item for item in data if item is not None]
