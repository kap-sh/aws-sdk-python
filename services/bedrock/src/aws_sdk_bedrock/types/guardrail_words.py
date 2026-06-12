"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_word

GuardrailWords: TypeAlias = list["aws_sdk_bedrock.types.guardrail_word.GuardrailWord"]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWords) -> list:
    import aws_sdk_bedrock.types.guardrail_word

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.guardrail_word.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailWords:
    import aws_sdk_bedrock.types.guardrail_word

    out: GuardrailWords = []
    for item in data:
        out.append(aws_sdk_bedrock.types.guardrail_word.deserialize_json(item))
    return out
