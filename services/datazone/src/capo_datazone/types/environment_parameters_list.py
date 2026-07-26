"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.environment_parameter

EnvironmentParametersList: TypeAlias = list[
    "capo_datazone.types.environment_parameter.EnvironmentParameter"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentParametersList) -> list:
    import capo_datazone.types.environment_parameter

    out: list = []
    for item in value:
        out.append(capo_datazone.types.environment_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentParametersList:
    import capo_datazone.types.environment_parameter

    out: EnvironmentParametersList = []
    for item in data:
        out.append(capo_datazone.types.environment_parameter.deserialize_json(item))
    return out
