"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartMarkerStyleSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.line_chart_marker_shape
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.visibility


class LineChartMarkerStyleSettings(TypedDict):
    marker_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Configuration option that determines whether to show the markers in the series.</p>"""
    marker_shape: NotRequired[
        "aws_sdk_quicksight.types.line_chart_marker_shape.LineChartMarkerShape"
    ]
    """<p>Shape option for markers in the series.</p> <ul> <li> <p> <code>CIRCLE</code>: Show marker as a circle.</p> </li> <li> <p> <code>TRIANGLE</code>: Show marker as a triangle.</p> </li> <li> <p> <code>SQUARE</code>: Show marker as a square.</p> </li> <li> <p> <code>DIAMOND</code>: Show marker as a diamond.</p> </li> <li> <p> <code>ROUNDED_SQUARE</code>: Show marker as a rounded square.</p> </li> </ul>"""
    marker_size: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>Size of marker in the series.</p>"""
    marker_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Color of marker in the series.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartMarkerStyleSettings) -> dict:
    out: dict = {}
    if "marker_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["MarkerVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["marker_visibility"]
        )
    if "marker_shape" in value:
        import aws_sdk_quicksight.types.line_chart_marker_shape

        out["MarkerShape"] = (
            aws_sdk_quicksight.types.line_chart_marker_shape.serialize_json(
                value["marker_shape"]
            )
        )
    if "marker_size" in value:
        out["MarkerSize"] = value["marker_size"]
    if "marker_color" in value:
        out["MarkerColor"] = value["marker_color"]
    return out


def deserialize_json(data: dict) -> LineChartMarkerStyleSettings:
    out: LineChartMarkerStyleSettings = {}  # type: ignore[typeddict-item]
    if "MarkerVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["marker_visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["MarkerVisibility"]
        )
    if "MarkerShape" in data:
        import aws_sdk_quicksight.types.line_chart_marker_shape

        out["marker_shape"] = (
            aws_sdk_quicksight.types.line_chart_marker_shape.deserialize_json(
                data["MarkerShape"]
            )
        )
    if "MarkerSize" in data:
        out["marker_size"] = data["MarkerSize"]
    if "MarkerColor" in data:
        out["marker_color"] = data["MarkerColor"]
    return out
