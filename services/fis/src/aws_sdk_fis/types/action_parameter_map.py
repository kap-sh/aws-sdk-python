"""Generated from Smithy shape ``com.amazonaws.fis#ActionParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.action_parameter
    import aws_sdk_fis.types.action_parameter_name

ActionParameterMap: TypeAlias = dict[
    "aws_sdk_fis.types.action_parameter_name.ActionParameterName",
    "aws_sdk_fis.types.action_parameter.ActionParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ActionParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fis.types.action_parameter

        out[key] = aws_sdk_fis.types.action_parameter.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ActionParameterMap:
    out: ActionParameterMap = {}
    for key, value in data.items():
        import aws_sdk_fis.types.action_parameter

        out[key] = aws_sdk_fis.types.action_parameter.deserialize_json(value)
    return out
