"""Generated from Smithy shape ``com.amazonaws.quicksight#SeriesItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.series_item

SeriesItemList: TypeAlias = list["aws_sdk_quicksight.types.series_item.SeriesItem"]


# --- restJson1 ser/de ---
def serialize_json(value: SeriesItemList) -> list:
    import aws_sdk_quicksight.types.series_item

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.series_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SeriesItemList:
    import aws_sdk_quicksight.types.series_item

    out: SeriesItemList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.series_item.deserialize_json(item))
    return out
