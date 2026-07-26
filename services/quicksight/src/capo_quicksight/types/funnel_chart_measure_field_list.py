"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartMeasureFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.measure_field

FunnelChartMeasureFieldList: TypeAlias = list[
    "capo_quicksight.types.measure_field.MeasureField"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartMeasureFieldList) -> list:
    import capo_quicksight.types.measure_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.measure_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunnelChartMeasureFieldList:
    import capo_quicksight.types.measure_field

    out: FunnelChartMeasureFieldList = []
    for item in data:
        out.append(capo_quicksight.types.measure_field.deserialize_json(item))
    return out
