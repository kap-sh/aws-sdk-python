"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ApiParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.api_parameter

ApiParameters: TypeAlias = list[
    "aws_sdk_bedrock_agent_runtime.types.api_parameter.ApiParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiParameters) -> list:
    import aws_sdk_bedrock_agent_runtime.types.api_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.api_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ApiParameters:
    import aws_sdk_bedrock_agent_runtime.types.api_parameter

    out: ApiParameters = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agent_runtime.types.api_parameter.deserialize_json(item)
        )
    return out
