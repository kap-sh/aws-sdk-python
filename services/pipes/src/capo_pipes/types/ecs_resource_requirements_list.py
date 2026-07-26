"""Generated from Smithy shape ``com.amazonaws.pipes#EcsResourceRequirementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.ecs_resource_requirement

EcsResourceRequirementsList: TypeAlias = list[
    "capo_pipes.types.ecs_resource_requirement.EcsResourceRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: EcsResourceRequirementsList) -> list:
    import capo_pipes.types.ecs_resource_requirement

    out: list = []
    for item in value:
        out.append(capo_pipes.types.ecs_resource_requirement.serialize_json(item))
    return out


def deserialize_json(data: list) -> EcsResourceRequirementsList:
    import capo_pipes.types.ecs_resource_requirement

    out: EcsResourceRequirementsList = []
    for item in data:
        out.append(capo_pipes.types.ecs_resource_requirement.deserialize_json(item))
    return out
