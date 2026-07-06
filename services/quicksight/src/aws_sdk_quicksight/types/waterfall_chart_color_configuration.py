"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartColorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.waterfall_chart_group_color_configuration


class WaterfallChartColorConfiguration(TypedDict, closed=True):
    group_color_configuration: NotRequired[
        "aws_sdk_quicksight.types.waterfall_chart_group_color_configuration.WaterfallChartGroupColorConfiguration"
    ]
    """<p>The color configuration for individual groups within a waterfall visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartColorConfiguration) -> dict:
    out: dict = {}
    if "group_color_configuration" in value:
        import aws_sdk_quicksight.types.waterfall_chart_group_color_configuration

        out["GroupColorConfiguration"] = (
            aws_sdk_quicksight.types.waterfall_chart_group_color_configuration.serialize_json(
                value["group_color_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaterfallChartColorConfiguration:
    out: WaterfallChartColorConfiguration = {}  # type: ignore[typeddict-item]
    if "GroupColorConfiguration" in data:
        import aws_sdk_quicksight.types.waterfall_chart_group_color_configuration

        out["group_color_configuration"] = (
            aws_sdk_quicksight.types.waterfall_chart_group_color_configuration.deserialize_json(
                data["GroupColorConfiguration"]
            )
        )
    return out
