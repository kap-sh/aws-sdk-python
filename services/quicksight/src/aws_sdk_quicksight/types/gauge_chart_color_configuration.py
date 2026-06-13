"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartColorConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color


class GaugeChartColorConfiguration(TypedDict):
    foreground_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The foreground color configuration of a <code>GaugeChartVisual</code>.</p>"""
    background_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The background color configuration of a <code>GaugeChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartColorConfiguration) -> dict:
    out: dict = {}
    if "foreground_color" in value:
        out["ForegroundColor"] = value["foreground_color"]
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    return out


def deserialize_json(data: dict) -> GaugeChartColorConfiguration:
    out: GaugeChartColorConfiguration = {}  # type: ignore[typeddict-item]
    if "ForegroundColor" in data:
        out["foreground_color"] = data["ForegroundColor"]
    if "BackgroundColor" in data:
        out["background_color"] = data["BackgroundColor"]
    return out
