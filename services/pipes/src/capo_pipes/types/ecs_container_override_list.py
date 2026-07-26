"""Generated from Smithy shape ``com.amazonaws.pipes#EcsContainerOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.ecs_container_override

EcsContainerOverrideList: TypeAlias = list[
    "capo_pipes.types.ecs_container_override.EcsContainerOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsContainerOverrideList) -> list:
    import capo_pipes.types.ecs_container_override

    out: list = []
    for item in value:
        out.append(capo_pipes.types.ecs_container_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> EcsContainerOverrideList:
    import capo_pipes.types.ecs_container_override

    out: EcsContainerOverrideList = []
    for item in data:
        out.append(capo_pipes.types.ecs_container_override.deserialize_json(item))
    return out
