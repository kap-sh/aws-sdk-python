"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailPiiEntityFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter

GuardrailPiiEntityFilterList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter.GuardrailPiiEntityFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntityFilterList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailPiiEntityFilterList:
    import aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter

    out: GuardrailPiiEntityFilterList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_pii_entity_filter.deserialize_json(
                item
            )
        )
    return out
