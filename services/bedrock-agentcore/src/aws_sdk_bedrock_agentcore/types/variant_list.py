"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#VariantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.variant

VariantList: TypeAlias = list["aws_sdk_bedrock_agentcore.types.variant.Variant"]


# --- restJson1 ser/de ---
def serialize_json(value: VariantList) -> list:
    import aws_sdk_bedrock_agentcore.types.variant

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.variant.serialize_json(item))
    return out


def deserialize_json(data: list) -> VariantList:
    import aws_sdk_bedrock_agentcore.types.variant

    out: VariantList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.variant.deserialize_json(item))
    return out
