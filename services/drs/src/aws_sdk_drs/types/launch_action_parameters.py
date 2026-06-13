"""Generated from Smithy shape ``com.amazonaws.drs#LaunchActionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.launch_action_parameter
    import aws_sdk_drs.types.launch_action_parameter_name

LaunchActionParameters: TypeAlias = dict[
    "aws_sdk_drs.types.launch_action_parameter_name.LaunchActionParameterName",
    "aws_sdk_drs.types.launch_action_parameter.LaunchActionParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LaunchActionParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_drs.types.launch_action_parameter

        out[key] = aws_sdk_drs.types.launch_action_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> LaunchActionParameters:
    out: LaunchActionParameters = {}
    for key, value in data.items():
        import aws_sdk_drs.types.launch_action_parameter

        out[key] = aws_sdk_drs.types.launch_action_parameter.deserialize_json(value)
    return out
