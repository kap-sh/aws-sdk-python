"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartLineStyleSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.line_chart_line_style
    import capo_quicksight.types.line_interpolation
    import capo_quicksight.types.pixel_length
    import capo_quicksight.types.visibility


class LineChartLineStyleSettings(TypedDict, closed=True):
    line_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Configuration option that determines whether to show the line for the series.</p>"""
    line_interpolation: NotRequired[
        "capo_quicksight.types.line_interpolation.LineInterpolation"
    ]
    """<p>Interpolation style for line series.</p> <ul> <li> <p> <code>LINEAR</code>: Show as default, linear style.</p> </li> <li> <p> <code>SMOOTH</code>: Show as a smooth curve.</p> </li> <li> <p> <code>STEPPED</code>: Show steps in line.</p> </li> </ul>"""
    line_style: NotRequired[
        "capo_quicksight.types.line_chart_line_style.LineChartLineStyle"
    ]
    """<p>Line style for line series.</p> <ul> <li> <p> <code>SOLID</code>: Show as a solid line.</p> </li> <li> <p> <code>DOTTED</code>: Show as a dotted line.</p> </li> <li> <p> <code>DASHED</code>: Show as a dashed line.</p> </li> </ul>"""
    line_width: NotRequired["capo_quicksight.types.pixel_length.PixelLength"]
    """<p>Width that determines the line thickness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartLineStyleSettings) -> dict:
    out: dict = {}
    if "line_visibility" in value:
        import capo_quicksight.types.visibility

        out["LineVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["line_visibility"]
        )
    if "line_interpolation" in value:
        import capo_quicksight.types.line_interpolation

        out["LineInterpolation"] = (
            capo_quicksight.types.line_interpolation.serialize_json(
                value["line_interpolation"]
            )
        )
    if "line_style" in value:
        import capo_quicksight.types.line_chart_line_style

        out["LineStyle"] = capo_quicksight.types.line_chart_line_style.serialize_json(
            value["line_style"]
        )
    if "line_width" in value:
        out["LineWidth"] = value["line_width"]
    return out


def deserialize_json(data: dict) -> LineChartLineStyleSettings:
    out: LineChartLineStyleSettings = {}  # type: ignore[typeddict-item]
    if "LineVisibility" in data:
        import capo_quicksight.types.visibility

        out["line_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["LineVisibility"]
        )
    if "LineInterpolation" in data:
        import capo_quicksight.types.line_interpolation

        out["line_interpolation"] = (
            capo_quicksight.types.line_interpolation.deserialize_json(
                data["LineInterpolation"]
            )
        )
    if "LineStyle" in data:
        import capo_quicksight.types.line_chart_line_style

        out["line_style"] = (
            capo_quicksight.types.line_chart_line_style.deserialize_json(
                data["LineStyle"]
            )
        )
    if "LineWidth" in data:
        out["line_width"] = data["LineWidth"]
    return out
