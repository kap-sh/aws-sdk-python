"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOriginList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_origin

GuardrailOriginList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_origin.GuardrailOrigin"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOriginList) -> list:
    import capo_bedrock_runtime.types.guardrail_origin

    out: list = []
    for item in value:
        out.append(capo_bedrock_runtime.types.guardrail_origin.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailOriginList:
    import capo_bedrock_runtime.types.guardrail_origin

    out: GuardrailOriginList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_runtime.types.guardrail_origin.deserialize_json(item))
    return out
