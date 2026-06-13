"""Generated from Smithy shape ``com.amazonaws.quicksight#SetParameterValueConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.set_parameter_value_configuration

SetParameterValueConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.set_parameter_value_configuration.SetParameterValueConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: SetParameterValueConfigurationList) -> list:
    import aws_sdk_quicksight.types.set_parameter_value_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.set_parameter_value_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SetParameterValueConfigurationList:
    import aws_sdk_quicksight.types.set_parameter_value_configuration

    out: SetParameterValueConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.set_parameter_value_configuration.deserialize_json(
                item
            )
        )
    return out
