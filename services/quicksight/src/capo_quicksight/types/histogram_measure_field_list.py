"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramMeasureFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.measure_field

HistogramMeasureFieldList: TypeAlias = list[
    "capo_quicksight.types.measure_field.MeasureField"
]


# --- restJson1 ser/de ---
def serialize_json(value: HistogramMeasureFieldList) -> list:
    import capo_quicksight.types.measure_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.measure_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> HistogramMeasureFieldList:
    import capo_quicksight.types.measure_field

    out: HistogramMeasureFieldList = []
    for item in data:
        out.append(capo_quicksight.types.measure_field.deserialize_json(item))
    return out
