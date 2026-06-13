"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseContentQualifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier

GuardrailConverseContentQualifierList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier.GuardrailConverseContentQualifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseContentQualifierList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailConverseContentQualifierList:
    import aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier

    out: GuardrailConverseContentQualifierList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_converse_content_qualifier.deserialize_json(
                item
            )
        )
    return out
