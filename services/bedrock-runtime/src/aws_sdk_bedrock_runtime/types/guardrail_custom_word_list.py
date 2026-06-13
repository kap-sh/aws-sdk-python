"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailCustomWordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_custom_word

GuardrailCustomWordList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_custom_word.GuardrailCustomWord"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCustomWordList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_custom_word

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_custom_word.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailCustomWordList:
    import aws_sdk_bedrock_runtime.types.guardrail_custom_word

    out: GuardrailCustomWordList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_custom_word.deserialize_json(item)
        )
    return out
