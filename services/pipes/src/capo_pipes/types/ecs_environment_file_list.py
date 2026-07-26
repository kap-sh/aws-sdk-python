"""Generated from Smithy shape ``com.amazonaws.pipes#EcsEnvironmentFileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.ecs_environment_file

EcsEnvironmentFileList: TypeAlias = list[
    "capo_pipes.types.ecs_environment_file.EcsEnvironmentFile"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsEnvironmentFileList) -> list:
    import capo_pipes.types.ecs_environment_file

    out: list = []
    for item in value:
        out.append(capo_pipes.types.ecs_environment_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> EcsEnvironmentFileList:
    import capo_pipes.types.ecs_environment_file

    out: EcsEnvironmentFileList = []
    for item in data:
        out.append(capo_pipes.types.ecs_environment_file.deserialize_json(item))
    return out
