"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartValuesFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.measure_field

RadarChartValuesFieldList: TypeAlias = list[
    "capo_quicksight.types.measure_field.MeasureField"
]


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartValuesFieldList) -> list:
    import capo_quicksight.types.measure_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.measure_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> RadarChartValuesFieldList:
    import capo_quicksight.types.measure_field

    out: RadarChartValuesFieldList = []
    for item in data:
        out.append(capo_quicksight.types.measure_field.deserialize_json(item))
    return out
