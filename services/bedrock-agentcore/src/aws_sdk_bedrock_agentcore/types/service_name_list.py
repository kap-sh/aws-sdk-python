"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ServiceNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.service_name

ServiceNameList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.service_name.ServiceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceNameList:
    return list(data)
