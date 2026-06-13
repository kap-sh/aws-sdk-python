"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_parameter

EnvironmentParametersList: TypeAlias = list[
    "aws_sdk_datazone.types.environment_parameter.EnvironmentParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentParametersList) -> list:
    import aws_sdk_datazone.types.environment_parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.environment_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentParametersList:
    import aws_sdk_datazone.types.environment_parameter

    out: EnvironmentParametersList = []
    for item in data:
        out.append(aws_sdk_datazone.types.environment_parameter.deserialize_json(item))
    return out
