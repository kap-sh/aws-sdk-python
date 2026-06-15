"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CustomRequestParametersType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.custom_request_key_type
    import aws_sdk_bedrock_agentcore.types.custom_request_value_type

CustomRequestParametersType: TypeAlias = dict[
    "aws_sdk_bedrock_agentcore.types.custom_request_key_type.CustomRequestKeyType",
    "aws_sdk_bedrock_agentcore.types.custom_request_value_type.CustomRequestValueType",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomRequestParametersType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CustomRequestParametersType:
    out: CustomRequestParametersType = {}
    for key, value in data.items():
        out[key] = value
    return out
