"""Generated from Smithy shape ``com.amazonaws.quicksight#AxisLabelOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.axis_label_options

AxisLabelOptionsList: TypeAlias = list[
    "capo_quicksight.types.axis_label_options.AxisLabelOptions"
]


# --- restJson1 ser/de ---
def serialize_json(value: AxisLabelOptionsList) -> list:
    import capo_quicksight.types.axis_label_options

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.axis_label_options.serialize_json(item))
    return out


def deserialize_json(data: list) -> AxisLabelOptionsList:
    import capo_quicksight.types.axis_label_options

    out: AxisLabelOptionsList = []
    for item in data:
        out.append(capo_quicksight.types.axis_label_options.deserialize_json(item))
    return out
