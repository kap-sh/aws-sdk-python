"""Generated from Smithy shape ``com.amazonaws.deadline#StepParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.step_parameter

StepParameterList: TypeAlias = list["capo_deadline.types.step_parameter.StepParameter"]


# --- restJson1 ser/de ---
def serialize_json(value: StepParameterList) -> list:
    import capo_deadline.types.step_parameter

    out: list = []
    for item in value:
        out.append(capo_deadline.types.step_parameter.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepParameterList:
    import capo_deadline.types.step_parameter

    out: StepParameterList = []
    for item in data:
        out.append(capo_deadline.types.step_parameter.deserialize_json(item))
    return out
