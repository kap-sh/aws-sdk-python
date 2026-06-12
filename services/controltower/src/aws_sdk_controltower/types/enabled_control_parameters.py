"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_control_parameter

EnabledControlParameters: TypeAlias = list[
    "aws_sdk_controltower.types.enabled_control_parameter.EnabledControlParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlParameters) -> list:
    import aws_sdk_controltower.types.enabled_control_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controltower.types.enabled_control_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnabledControlParameters:
    import aws_sdk_controltower.types.enabled_control_parameter

    out: EnabledControlParameters = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.enabled_control_parameter.deserialize_json(item)
        )
    return out
