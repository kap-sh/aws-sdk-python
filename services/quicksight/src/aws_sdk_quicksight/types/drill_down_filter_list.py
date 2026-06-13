"""Generated from Smithy shape ``com.amazonaws.quicksight#DrillDownFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.drill_down_filter

DrillDownFilterList: TypeAlias = list[
    "aws_sdk_quicksight.types.drill_down_filter.DrillDownFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: DrillDownFilterList) -> list:
    import aws_sdk_quicksight.types.drill_down_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.drill_down_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> DrillDownFilterList:
    import aws_sdk_quicksight.types.drill_down_filter

    out: DrillDownFilterList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.drill_down_filter.deserialize_json(item))
    return out
