"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailPiiEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_pii_entity

GuardrailPiiEntities: TypeAlias = list[
    "capo_bedrock.types.guardrail_pii_entity.GuardrailPiiEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntities) -> list:
    import capo_bedrock.types.guardrail_pii_entity

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.guardrail_pii_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailPiiEntities:
    import capo_bedrock.types.guardrail_pii_entity

    out: GuardrailPiiEntities = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.guardrail_pii_entity.deserialize_json(item))
    return out
