"""Generated from Smithy shape ``com.amazonaws.pipes#EcsEnvironmentFileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.ecs_environment_file

EcsEnvironmentFileList: TypeAlias = list[
    "aws_sdk_pipes.types.ecs_environment_file.EcsEnvironmentFile"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsEnvironmentFileList) -> list:
    import aws_sdk_pipes.types.ecs_environment_file

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.ecs_environment_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> EcsEnvironmentFileList:
    import aws_sdk_pipes.types.ecs_environment_file

    out: EcsEnvironmentFileList = []
    for item in data:
        out.append(aws_sdk_pipes.types.ecs_environment_file.deserialize_json(item))
    return out
