"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentBlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_content_block

GuardrailContentBlockList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_content_block.GuardrailContentBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentBlockList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_content_block

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_content_block.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailContentBlockList:
    import aws_sdk_bedrock_runtime.types.guardrail_content_block

    out: GuardrailContentBlockList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_content_block.deserialize_json(item)
        )
    return out
