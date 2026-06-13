"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartValuesFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.measure_field

RadarChartValuesFieldList: TypeAlias = list[
    "aws_sdk_quicksight.types.measure_field.MeasureField"
]


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartValuesFieldList) -> list:
    import aws_sdk_quicksight.types.measure_field

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.measure_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> RadarChartValuesFieldList:
    import aws_sdk_quicksight.types.measure_field

    out: RadarChartValuesFieldList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.measure_field.deserialize_json(item))
    return out
