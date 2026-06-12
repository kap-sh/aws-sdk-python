"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailPiiEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_pii_entity

GuardrailPiiEntities: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_pii_entity.GuardrailPiiEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntities) -> list:
    import aws_sdk_bedrock.types.guardrail_pii_entity

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.guardrail_pii_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailPiiEntities:
    import aws_sdk_bedrock.types.guardrail_pii_entity

    out: GuardrailPiiEntities = []
    for item in data:
        out.append(aws_sdk_bedrock.types.guardrail_pii_entity.deserialize_json(item))
    return out
