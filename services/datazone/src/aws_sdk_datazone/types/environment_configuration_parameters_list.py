"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_configuration_parameter

EnvironmentConfigurationParametersList: TypeAlias = list[
    "aws_sdk_datazone.types.environment_configuration_parameter.EnvironmentConfigurationParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationParametersList) -> list:
    import aws_sdk_datazone.types.environment_configuration_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.environment_configuration_parameter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnvironmentConfigurationParametersList:
    import aws_sdk_datazone.types.environment_configuration_parameter

    out: EnvironmentConfigurationParametersList = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.environment_configuration_parameter.deserialize_json(
                item
            )
        )
    return out
