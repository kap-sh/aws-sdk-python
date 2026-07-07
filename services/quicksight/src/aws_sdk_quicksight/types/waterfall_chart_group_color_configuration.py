"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartGroupColorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color


class WaterfallChartGroupColorConfiguration(TypedDict, closed=True):
    positive_bar_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Defines the color for the positive bars of a waterfall chart.</p>"""
    negative_bar_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Defines the color for the negative bars of a waterfall chart.</p>"""
    total_bar_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Defines the color for the total bars of a waterfall chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartGroupColorConfiguration) -> dict:
    out: dict = {}
    if "positive_bar_color" in value:
        out["PositiveBarColor"] = value["positive_bar_color"]
    if "negative_bar_color" in value:
        out["NegativeBarColor"] = value["negative_bar_color"]
    if "total_bar_color" in value:
        out["TotalBarColor"] = value["total_bar_color"]
    return out


def deserialize_json(data: dict) -> WaterfallChartGroupColorConfiguration:
    out: WaterfallChartGroupColorConfiguration = {}  # type: ignore[typeddict-item]
    if "PositiveBarColor" in data:
        out["positive_bar_color"] = data["PositiveBarColor"]
    if "NegativeBarColor" in data:
        out["negative_bar_color"] = data["NegativeBarColor"]
    if "TotalBarColor" in data:
        out["total_bar_color"] = data["TotalBarColor"]
    return out
