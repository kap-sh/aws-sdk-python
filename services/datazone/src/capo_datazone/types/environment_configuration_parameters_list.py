"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_configuration_parameter

EnvironmentConfigurationParametersList: TypeAlias = list[
    "capo_datazone.types.environment_configuration_parameter.EnvironmentConfigurationParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationParametersList) -> list:
    import capo_datazone.types.environment_configuration_parameter

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.environment_configuration_parameter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnvironmentConfigurationParametersList:
    import capo_datazone.types.environment_configuration_parameter

    out: EnvironmentConfigurationParametersList = []
    for item in data:
        out.append(
            capo_datazone.types.environment_configuration_parameter.deserialize_json(
                item
            )
        )
    return out
