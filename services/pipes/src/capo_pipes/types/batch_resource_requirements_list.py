"""Generated from Smithy shape ``com.amazonaws.pipes#BatchResourceRequirementsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.batch_resource_requirement

BatchResourceRequirementsList: TypeAlias = list[
    "capo_pipes.types.batch_resource_requirement.BatchResourceRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchResourceRequirementsList) -> list:
    import capo_pipes.types.batch_resource_requirement

    out: list = []
    for item in value:
        out.append(capo_pipes.types.batch_resource_requirement.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchResourceRequirementsList:
    import capo_pipes.types.batch_resource_requirement

    out: BatchResourceRequirementsList = []
    for item in data:
        out.append(capo_pipes.types.batch_resource_requirement.deserialize_json(item))
    return out
