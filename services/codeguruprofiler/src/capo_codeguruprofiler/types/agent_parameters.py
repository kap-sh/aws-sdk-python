"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AgentParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.agent_parameter_field

AgentParameters: TypeAlias = dict[
    "capo_codeguruprofiler.types.agent_parameter_field.AgentParameterField", "str"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AgentParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AgentParameters:
    out: AgentParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
