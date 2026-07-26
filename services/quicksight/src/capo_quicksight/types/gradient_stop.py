"""Generated from Smithy shape ``com.amazonaws.quicksight#GradientStop``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.hex_color


class GradientStop(TypedDict, closed=True):
    gradient_offset: "capo_quicksight.types.double.Double"
    """<p>Determines gradient offset value.</p>"""
    data_value: NotRequired["capo_quicksight.types.double.Double"]
    """<p>Determines the data value.</p>"""
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GradientStop) -> dict:
    out: dict = {}
    out["GradientOffset"] = value.get("gradient_offset", 0)
    if "data_value" in value:
        out["DataValue"] = value["data_value"]
    if "color" in value:
        out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> GradientStop:
    out: GradientStop = {}  # type: ignore[typeddict-item]
    if "GradientOffset" in data:
        out["gradient_offset"] = data["GradientOffset"]
    else:
        out["gradient_offset"] = 0
    if "DataValue" in data:
        out["data_value"] = data["DataValue"]
    if "Color" in data:
        out["color"] = data["Color"]
    return out
