"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AllowedQueryParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_query_parameter_name

AllowedQueryParameters: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.http_query_parameter_name.HttpQueryParameterName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedQueryParameters) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedQueryParameters:
    return list(data)
