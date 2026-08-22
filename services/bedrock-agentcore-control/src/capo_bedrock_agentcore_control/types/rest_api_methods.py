"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RestApiMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.rest_api_method

RestApiMethods: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.rest_api_method.RestApiMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: RestApiMethods) -> list:
    import capo_bedrock_agentcore_control.types.rest_api_method

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.rest_api_method.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RestApiMethods:
    import capo_bedrock_agentcore_control.types.rest_api_method

    out: RestApiMethods = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.rest_api_method.deserialize_json(item)
        )
    return out
