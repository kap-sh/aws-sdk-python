"""Generated from Smithy shape ``com.amazonaws.quicksight#DataColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.hex_color


class DataColor(TypedDict, closed=True):
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color that is applied to the data value.</p>"""
    data_value: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The data value that the color is applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataColor) -> dict:
    out: dict = {}
    if "color" in value:
        out["Color"] = value["color"]
    if "data_value" in value:
        out["DataValue"] = value["data_value"]
    return out


def deserialize_json(data: dict) -> DataColor:
    out: DataColor = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    if "DataValue" in data:
        out["data_value"] = data["DataValue"]
    return out
