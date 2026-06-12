"""Generated from Smithy shape ``com.amazonaws.pipes#EcsContainerOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.ecs_container_override

EcsContainerOverrideList: TypeAlias = list[
    "aws_sdk_pipes.types.ecs_container_override.EcsContainerOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsContainerOverrideList) -> list:
    import aws_sdk_pipes.types.ecs_container_override

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.ecs_container_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> EcsContainerOverrideList:
    import aws_sdk_pipes.types.ecs_container_override

    out: EcsContainerOverrideList = []
    for item in data:
        out.append(aws_sdk_pipes.types.ecs_container_override.deserialize_json(item))
    return out
