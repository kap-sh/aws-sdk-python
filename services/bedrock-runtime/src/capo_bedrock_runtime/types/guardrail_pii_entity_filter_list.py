"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailPiiEntityFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_pii_entity_filter

GuardrailPiiEntityFilterList: TypeAlias = list[
    "capo_bedrock_runtime.types.guardrail_pii_entity_filter.GuardrailPiiEntityFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntityFilterList) -> list:
    import capo_bedrock_runtime.types.guardrail_pii_entity_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_runtime.types.guardrail_pii_entity_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailPiiEntityFilterList:
    import capo_bedrock_runtime.types.guardrail_pii_entity_filter

    out: GuardrailPiiEntityFilterList = []
    for item in data:
        out.append(
            capo_bedrock_runtime.types.guardrail_pii_entity_filter.deserialize_json(
                item
            )
        )
    return out
