"""Generated from Smithy shape ``com.amazonaws.quicksight#SeriesItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.series_item

SeriesItemList: TypeAlias = list["capo_quicksight.types.series_item.SeriesItem"]


# --- restJson1 ser/de ---
def serialize_json(value: SeriesItemList) -> list:
    import capo_quicksight.types.series_item

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.series_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SeriesItemList:
    import capo_quicksight.types.series_item

    out: SeriesItemList = []
    for item in data:
        out.append(capo_quicksight.types.series_item.deserialize_json(item))
    return out
