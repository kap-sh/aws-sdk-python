"""Generated from Smithy shape ``com.amazonaws.deadline#StepDependencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.step_dependency

StepDependencies: TypeAlias = list["capo_deadline.types.step_dependency.StepDependency"]


# --- restJson1 ser/de ---
def serialize_json(value: StepDependencies) -> list:
    import capo_deadline.types.step_dependency

    out: list = []
    for item in value:
        out.append(capo_deadline.types.step_dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepDependencies:
    import capo_deadline.types.step_dependency

    out: StepDependencies = []
    for item in data:
        out.append(capo_deadline.types.step_dependency.deserialize_json(item))
    return out
