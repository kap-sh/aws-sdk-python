"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.launch_action_parameter
    import capo_drs.types.launch_action_parameter_name

LaunchActionParameters: TypeAlias = dict[
    "capo_drs.types.launch_action_parameter_name.LaunchActionParameterName",
    "capo_drs.types.launch_action_parameter.LaunchActionParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LaunchActionParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_drs.types.launch_action_parameter

        out[key] = capo_drs.types.launch_action_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LaunchActionParameters:
    out: LaunchActionParameters = {}
    for key, value in data.items():
        import capo_drs.types.launch_action_parameter

        out[key] = capo_drs.types.launch_action_parameter.deserialize_json(value)
    return out
