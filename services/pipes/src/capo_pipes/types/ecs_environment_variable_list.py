"""Generated from Smithy shape ``com.amazonaws.pipes#EcsEnvironmentVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.ecs_environment_variable

EcsEnvironmentVariableList: TypeAlias = list[
    "capo_pipes.types.ecs_environment_variable.EcsEnvironmentVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsEnvironmentVariableList) -> list:
    import capo_pipes.types.ecs_environment_variable

    out: list = []
    for item in value:
        out.append(capo_pipes.types.ecs_environment_variable.serialize_json(item))
    return out


def deserialize_json(data: list) -> EcsEnvironmentVariableList:
    import capo_pipes.types.ecs_environment_variable

    out: EcsEnvironmentVariableList = []
    for item in data:
        out.append(capo_pipes.types.ecs_environment_variable.deserialize_json(item))
    return out
