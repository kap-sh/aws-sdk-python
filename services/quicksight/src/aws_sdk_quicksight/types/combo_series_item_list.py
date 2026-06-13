"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboSeriesItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.combo_series_item

ComboSeriesItemList: TypeAlias = list[
    "aws_sdk_quicksight.types.combo_series_item.ComboSeriesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComboSeriesItemList) -> list:
    import aws_sdk_quicksight.types.combo_series_item

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.combo_series_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComboSeriesItemList:
    import aws_sdk_quicksight.types.combo_series_item

    out: ComboSeriesItemList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.combo_series_item.deserialize_json(item))
    return out
