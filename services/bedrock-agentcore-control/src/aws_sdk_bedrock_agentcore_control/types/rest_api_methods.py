"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RestApiMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.rest_api_method

RestApiMethods: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.rest_api_method.RestApiMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestApiMethods) -> list:
    import aws_sdk_bedrock_agentcore_control.types.rest_api_method

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.rest_api_method.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RestApiMethods:
    import aws_sdk_bedrock_agentcore_control.types.rest_api_method

    out: RestApiMethods = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.rest_api_method.deserialize_json(
                item
            )
        )
    return out
