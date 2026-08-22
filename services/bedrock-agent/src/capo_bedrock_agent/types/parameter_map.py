"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.name
    import capo_bedrock_agent.types.parameter_detail

ParameterMap: TypeAlias = dict[
    "capo_bedrock_agent.types.name.Name",
    "capo_bedrock_agent.types.parameter_detail.ParameterDetail",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock_agent.types.parameter_detail

        out[key] = capo_bedrock_agent.types.parameter_detail.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ParameterMap:
    out: ParameterMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_bedrock_agent.types.parameter_detail

        out[key] = capo_bedrock_agent.types.parameter_detail.deserialize_json(value)
    return out
