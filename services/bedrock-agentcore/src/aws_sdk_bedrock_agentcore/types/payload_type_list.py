"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PayloadTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payload_type

PayloadTypeList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.payload_type.PayloadType"
]


# --- restJson1 ser/de ---
def serialize_json(value: PayloadTypeList) -> list:
    import aws_sdk_bedrock_agentcore.types.payload_type

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.payload_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> PayloadTypeList:
    import aws_sdk_bedrock_agentcore.types.payload_type

    out: PayloadTypeList = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.payload_type.deserialize_json(item))
    return out
