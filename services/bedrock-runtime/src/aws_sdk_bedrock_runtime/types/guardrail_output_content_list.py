"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOutputContentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_output_content

GuardrailOutputContentList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_output_content.GuardrailOutputContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOutputContentList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_output_content

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_output_content.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailOutputContentList:
    import aws_sdk_bedrock_runtime.types.guardrail_output_content

    out: GuardrailOutputContentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_output_content.deserialize_json(
                item
            )
        )
    return out
