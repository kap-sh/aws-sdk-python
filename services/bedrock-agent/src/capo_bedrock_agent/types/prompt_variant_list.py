"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptVariantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_variant

PromptVariantList: TypeAlias = list[
    "capo_bedrock_agent.types.prompt_variant.PromptVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptVariantList) -> list:
    import capo_bedrock_agent.types.prompt_variant

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.prompt_variant.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptVariantList:
    import capo_bedrock_agent.types.prompt_variant

    out: PromptVariantList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.prompt_variant.deserialize_json(item))
    return out
