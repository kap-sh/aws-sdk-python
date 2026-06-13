"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_configuration

EnvironmentConfigurationsList: TypeAlias = list[
    "aws_sdk_datazone.types.environment_configuration.EnvironmentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationsList) -> list:
    import aws_sdk_datazone.types.environment_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.environment_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnvironmentConfigurationsList:
    import aws_sdk_datazone.types.environment_configuration

    out: EnvironmentConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.environment_configuration.deserialize_json(item)
        )
    return out
