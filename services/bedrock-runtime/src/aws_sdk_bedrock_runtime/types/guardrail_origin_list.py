"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOriginList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_origin

GuardrailOriginList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.guardrail_origin.GuardrailOrigin"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOriginList) -> list:
    import aws_sdk_bedrock_runtime.types.guardrail_origin

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_runtime.types.guardrail_origin.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailOriginList:
    import aws_sdk_bedrock_runtime.types.guardrail_origin

    out: GuardrailOriginList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_runtime.types.guardrail_origin.deserialize_json(item)
        )
    return out
