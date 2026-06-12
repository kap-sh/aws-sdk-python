"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptVariantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.prompt_variant

PromptVariantList: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.prompt_variant.PromptVariant"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptVariantList) -> list:
    import aws_sdk_bedrock_agent.types.prompt_variant

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.prompt_variant.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptVariantList:
    import aws_sdk_bedrock_agent.types.prompt_variant

    out: PromptVariantList = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.prompt_variant.deserialize_json(item))
    return out
