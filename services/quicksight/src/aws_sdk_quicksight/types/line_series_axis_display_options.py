"""Generated from Smithy shape ``com.amazonaws.quicksight#LineSeriesAxisDisplayOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_display_options
    import aws_sdk_quicksight.types.missing_data_configuration_list


class LineSeriesAxisDisplayOptions(TypedDict, closed=True):
    axis_options: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the line series axis.</p>"""
    missing_data_configurations: NotRequired[
        "aws_sdk_quicksight.types.missing_data_configuration_list.MissingDataConfigurationList"
    ]
    """<p>The configuration options that determine how missing data is treated during the rendering of a line chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineSeriesAxisDisplayOptions) -> dict:
    out: dict = {}
    if "axis_options" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["AxisOptions"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["axis_options"]
            )
        )
    if "missing_data_configurations" in value:
        import aws_sdk_quicksight.types.missing_data_configuration_list

        out["MissingDataConfigurations"] = (
            aws_sdk_quicksight.types.missing_data_configuration_list.serialize_json(
                value["missing_data_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineSeriesAxisDisplayOptions:
    out: LineSeriesAxisDisplayOptions = {}  # type: ignore[typeddict-item]
    if "AxisOptions" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["axis_options"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["AxisOptions"]
            )
        )
    if "MissingDataConfigurations" in data:
        import aws_sdk_quicksight.types.missing_data_configuration_list

        out["missing_data_configurations"] = (
            aws_sdk_quicksight.types.missing_data_configuration_list.deserialize_json(
                data["MissingDataConfigurations"]
            )
        )
    return out
