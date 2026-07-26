"""Generated from Smithy shape ``com.amazonaws.quicksight#ComputationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.computation

ComputationList: TypeAlias = list["capo_quicksight.types.computation.Computation"]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationList) -> list:
    import capo_quicksight.types.computation

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.computation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComputationList:
    import capo_quicksight.types.computation

    out: ComputationList = []
    for item in data:
        out.append(capo_quicksight.types.computation.deserialize_json(item))
    return out
