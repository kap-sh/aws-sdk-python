"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericAxisOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_display_range
    import aws_sdk_quicksight.types.axis_scale


class NumericAxisOptions(TypedDict):
    scale: NotRequired["aws_sdk_quicksight.types.axis_scale.AxisScale"]
    """<p>The scale setup of a numeric axis.</p>"""
    range: NotRequired["aws_sdk_quicksight.types.axis_display_range.AxisDisplayRange"]
    """<p>The range setup of a numeric axis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericAxisOptions) -> dict:
    out: dict = {}
    if "scale" in value:
        import aws_sdk_quicksight.types.axis_scale

        out["Scale"] = aws_sdk_quicksight.types.axis_scale.serialize_json(
            value["scale"]
        )
    if "range" in value:
        import aws_sdk_quicksight.types.axis_display_range

        out["Range"] = aws_sdk_quicksight.types.axis_display_range.serialize_json(
            value["range"]
        )
    return out


def deserialize_json(data: dict) -> NumericAxisOptions:
    out: NumericAxisOptions = {}  # type: ignore[typeddict-item]
    if "Scale" in data:
        import aws_sdk_quicksight.types.axis_scale

        out["scale"] = aws_sdk_quicksight.types.axis_scale.deserialize_json(
            data["Scale"]
        )
    if "Range" in data:
        import aws_sdk_quicksight.types.axis_display_range

        out["range"] = aws_sdk_quicksight.types.axis_display_range.deserialize_json(
            data["Range"]
        )
    return out
