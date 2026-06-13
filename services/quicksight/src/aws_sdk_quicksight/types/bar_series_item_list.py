"""Generated from Smithy shape ``com.amazonaws.quicksight#BarSeriesItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.bar_series_item

BarSeriesItemList: TypeAlias = list[
    "aws_sdk_quicksight.types.bar_series_item.BarSeriesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BarSeriesItemList) -> list:
    import aws_sdk_quicksight.types.bar_series_item

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.bar_series_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BarSeriesItemList:
    import aws_sdk_quicksight.types.bar_series_item

    out: BarSeriesItemList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.bar_series_item.deserialize_json(item))
    return out
