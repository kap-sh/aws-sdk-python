"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.box_plot_style_options
    import aws_sdk_quicksight.types.visibility


class BoxPlotOptions(TypedDict):
    style_options: NotRequired[
        "aws_sdk_quicksight.types.box_plot_style_options.BoxPlotStyleOptions"
    ]
    """<p>The style options of the box plot.</p>"""
    outlier_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the outlier in a box plot.</p>"""
    all_data_points_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines the visibility of all data points of the box plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotOptions) -> dict:
    out: dict = {}
    if "style_options" in value:
        import aws_sdk_quicksight.types.box_plot_style_options

        out["StyleOptions"] = (
            aws_sdk_quicksight.types.box_plot_style_options.serialize_json(
                value["style_options"]
            )
        )
    if "outlier_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["OutlierVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["outlier_visibility"]
        )
    if "all_data_points_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["AllDataPointsVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["all_data_points_visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> BoxPlotOptions:
    out: BoxPlotOptions = {}  # type: ignore[typeddict-item]
    if "StyleOptions" in data:
        import aws_sdk_quicksight.types.box_plot_style_options

        out["style_options"] = (
            aws_sdk_quicksight.types.box_plot_style_options.deserialize_json(
                data["StyleOptions"]
            )
        )
    if "OutlierVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["outlier_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["OutlierVisibility"]
            )
        )
    if "AllDataPointsVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["all_data_points_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["AllDataPointsVisibility"]
            )
        )
    return out
