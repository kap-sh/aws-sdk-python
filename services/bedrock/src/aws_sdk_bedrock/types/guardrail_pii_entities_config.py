"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailPiiEntitiesConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_pii_entity_config

GuardrailPiiEntitiesConfig: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_pii_entity_config.GuardrailPiiEntityConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntitiesConfig) -> list:
    import aws_sdk_bedrock.types.guardrail_pii_entity_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.guardrail_pii_entity_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailPiiEntitiesConfig:
    import aws_sdk_bedrock.types.guardrail_pii_entity_config

    out: GuardrailPiiEntitiesConfig = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.guardrail_pii_entity_config.deserialize_json(item)
        )
    return out
