"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#VariantResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.variant_result

VariantResultList: TypeAlias = list[
    "capo_bedrock_agentcore.types.variant_result.VariantResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: VariantResultList) -> list:
    import capo_bedrock_agentcore.types.variant_result

    out: list = []
    for item in value:
        out.append(capo_bedrock_agentcore.types.variant_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> VariantResultList:
    import capo_bedrock_agentcore.types.variant_result

    out: VariantResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agentcore.types.variant_result.deserialize_json(item))
    return out
