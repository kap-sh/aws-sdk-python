"""Generated from Smithy shape ``com.amazonaws.quicksight#TableInlineVisualization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_bars_options
    import aws_sdk_quicksight.types.sparklines_options


class TableInlineVisualization(TypedDict):
    data_bars: NotRequired["aws_sdk_quicksight.types.data_bars_options.DataBarsOptions"]
    """<p>The configuration of the inline visualization of the data bars within a chart.</p>"""
    sparklines: NotRequired[
        "aws_sdk_quicksight.types.sparklines_options.SparklinesOptions"
    ]
    """<p>The configuration of the inline visualization of the sparklines within a chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableInlineVisualization) -> dict:
    out: dict = {}
    if "data_bars" in value:
        import aws_sdk_quicksight.types.data_bars_options

        out["DataBars"] = aws_sdk_quicksight.types.data_bars_options.serialize_json(
            value["data_bars"]
        )
    if "sparklines" in value:
        import aws_sdk_quicksight.types.sparklines_options

        out["Sparklines"] = aws_sdk_quicksight.types.sparklines_options.serialize_json(
            value["sparklines"]
        )
    return out


def deserialize_json(data: dict) -> TableInlineVisualization:
    out: TableInlineVisualization = {}  # type: ignore[typeddict-item]
    if "DataBars" in data:
        import aws_sdk_quicksight.types.data_bars_options

        out["data_bars"] = aws_sdk_quicksight.types.data_bars_options.deserialize_json(
            data["DataBars"]
        )
    if "Sparklines" in data:
        import aws_sdk_quicksight.types.sparklines_options

        out["sparklines"] = (
            aws_sdk_quicksight.types.sparklines_options.deserialize_json(
                data["Sparklines"]
            )
        )
    return out
