"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.parameter_detail

ParameterMap: TypeAlias = dict[
    "aws_sdk_bedrock_agent.types.name.Name",
    "aws_sdk_bedrock_agent.types.parameter_detail.ParameterDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_bedrock_agent.types.parameter_detail

        out[key] = aws_sdk_bedrock_agent.types.parameter_detail.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ParameterMap:
    out: ParameterMap = {}
    for key, value in data.items():
        import aws_sdk_bedrock_agent.types.parameter_detail

        out[key] = aws_sdk_bedrock_agent.types.parameter_detail.deserialize_json(value)
    return out
