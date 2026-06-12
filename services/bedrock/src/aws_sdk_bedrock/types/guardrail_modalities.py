"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailModalities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_modality

GuardrailModalities: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_modality.GuardrailModality"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailModalities) -> list:
    import aws_sdk_bedrock.types.guardrail_modality

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.guardrail_modality.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailModalities:
    import aws_sdk_bedrock.types.guardrail_modality

    out: GuardrailModalities = []
    for item in data:
        out.append(aws_sdk_bedrock.types.guardrail_modality.deserialize_json(item))
    return out
