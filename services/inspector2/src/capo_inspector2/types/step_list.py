"""Generated from Smithy shape ``com.amazonaws.inspector2#StepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.step

StepList: TypeAlias = list["capo_inspector2.types.step.Step"]


# --- restJson1 ser/de ---
def serialize_json(value: StepList) -> list:
    import capo_inspector2.types.step

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.step.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepList:
    import capo_inspector2.types.step

    out: StepList = []
    for item in data:
        out.append(capo_inspector2.types.step.deserialize_json(item))
    return out
