"""Generated from Smithy shape ``com.amazonaws.pipes#EcsEnvironmentVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.ecs_environment_variable

EcsEnvironmentVariableList: TypeAlias = list[
    "aws_sdk_pipes.types.ecs_environment_variable.EcsEnvironmentVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsEnvironmentVariableList) -> list:
    import aws_sdk_pipes.types.ecs_environment_variable

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.ecs_environment_variable.serialize_json(item))
    return out


def deserialize_json(data: list) -> EcsEnvironmentVariableList:
    import aws_sdk_pipes.types.ecs_environment_variable

    out: EcsEnvironmentVariableList = []
    for item in data:
        out.append(aws_sdk_pipes.types.ecs_environment_variable.deserialize_json(item))
    return out
