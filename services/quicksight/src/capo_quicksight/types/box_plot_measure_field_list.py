"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotMeasureFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.measure_field

BoxPlotMeasureFieldList: TypeAlias = list[
    "capo_quicksight.types.measure_field.MeasureField"
]


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotMeasureFieldList) -> list:
    import capo_quicksight.types.measure_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.measure_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> BoxPlotMeasureFieldList:
    import capo_quicksight.types.measure_field

    out: BoxPlotMeasureFieldList = []
    for item in data:
        out.append(capo_quicksight.types.measure_field.deserialize_json(item))
    return out
