"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotStyleOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.box_plot_fill_style


class BoxPlotStyleOptions(TypedDict):
    fill_style: NotRequired[
        "aws_sdk_quicksight.types.box_plot_fill_style.BoxPlotFillStyle"
    ]
    """<p>The fill styles (solid, transparent) of the box plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotStyleOptions) -> dict:
    out: dict = {}
    if "fill_style" in value:
        import aws_sdk_quicksight.types.box_plot_fill_style

        out["FillStyle"] = aws_sdk_quicksight.types.box_plot_fill_style.serialize_json(
            value["fill_style"]
        )
    return out


def deserialize_json(data: dict) -> BoxPlotStyleOptions:
    out: BoxPlotStyleOptions = {}  # type: ignore[typeddict-item]
    if "FillStyle" in data:
        import aws_sdk_quicksight.types.box_plot_fill_style

        out["fill_style"] = (
            aws_sdk_quicksight.types.box_plot_fill_style.deserialize_json(
                data["FillStyle"]
            )
        )
    return out
