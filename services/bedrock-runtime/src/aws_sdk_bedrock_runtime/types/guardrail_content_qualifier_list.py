"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentQualifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_content_qualifier

GuardrailContentQualifierList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_content_qualifier.GuardrailContentQualifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentQualifierList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_content_qualifier

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_content_qualifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailContentQualifierList:
    import aws_sdk_bedrock_runtime.types.guardrail_content_qualifier

    out: GuardrailContentQualifierList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_content_qualifier.deserialize_json(
                item
            )
        )
    return out
