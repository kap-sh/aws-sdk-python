"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOutputContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_output_content

GuardrailOutputContentList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_output_content.GuardrailOutputContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOutputContentList) -> list:
    import capo_bedrock_runtime.types.guardrail_output_content

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_output_content.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailOutputContentList:
    import capo_bedrock_runtime.types.guardrail_output_content

    out: GuardrailOutputContentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_runtime.types.guardrail_output_content.deserialize_json(item)
        )
    return out
