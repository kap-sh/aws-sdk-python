"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorScaleColorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_color

ColorScaleColorList: TypeAlias = list["capo_quicksight.types.data_color.DataColor"]


# --- restJson1 ser/de ---
def serialize_json(value: ColorScaleColorList) -> list:
    import capo_quicksight.types.data_color

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_color.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColorScaleColorList:
    import capo_quicksight.types.data_color

    out: ColorScaleColorList = []
    for item in data:
        out.append(capo_quicksight.types.data_color.deserialize_json(item))
    return out
