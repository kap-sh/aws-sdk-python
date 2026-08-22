"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ApiContentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.property_parameters

ApiContentMap: TypeAlias = dict[
    "str", "capo_bedrock_agent_runtime.types.property_parameters.PropertyParameters"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ApiContentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock_agent_runtime.types.property_parameters

        out[key] = capo_bedrock_agent_runtime.types.property_parameters.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> ApiContentMap:
    out: ApiContentMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_bedrock_agent_runtime.types.property_parameters

        out[key] = (
            capo_bedrock_agent_runtime.types.property_parameters.deserialize_json(value)
        )
    return out
