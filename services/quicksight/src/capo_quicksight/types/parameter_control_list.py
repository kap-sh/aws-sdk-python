"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterControlList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.parameter_control

ParameterControlList: TypeAlias = list[
    "capo_quicksight.types.parameter_control.ParameterControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterControlList) -> list:
    import capo_quicksight.types.parameter_control

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.parameter_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParameterControlList:
    import capo_quicksight.types.parameter_control

    out: ParameterControlList = []
    for item in data:
        out.append(capo_quicksight.types.parameter_control.deserialize_json(item))
    return out
