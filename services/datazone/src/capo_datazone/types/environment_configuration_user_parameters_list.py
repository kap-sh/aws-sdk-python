"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationUserParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_configuration_user_parameter

EnvironmentConfigurationUserParametersList: TypeAlias = list[
    "capo_datazone.types.environment_configuration_user_parameter.EnvironmentConfigurationUserParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationUserParametersList) -> list:
    import capo_datazone.types.environment_configuration_user_parameter

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.environment_configuration_user_parameter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnvironmentConfigurationUserParametersList:
    import capo_datazone.types.environment_configuration_user_parameter

    out: EnvironmentConfigurationUserParametersList = []
    for item in data:
        out.append(
            capo_datazone.types.environment_configuration_user_parameter.deserialize_json(
                item
            )
        )
    return out
