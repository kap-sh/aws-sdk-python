"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.box_plot_aggregated_field_wells


class BoxPlotFieldWells(TypedDict):
    box_plot_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.box_plot_aggregated_field_wells.BoxPlotAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a box plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotFieldWells) -> dict:
    out: dict = {}
    if "box_plot_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.box_plot_aggregated_field_wells

        out["BoxPlotAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.box_plot_aggregated_field_wells.serialize_json(
                value["box_plot_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> BoxPlotFieldWells:
    out: BoxPlotFieldWells = {}  # type: ignore[typeddict-item]
    if "BoxPlotAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.box_plot_aggregated_field_wells

        out["box_plot_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.box_plot_aggregated_field_wells.deserialize_json(
                data["BoxPlotAggregatedFieldWells"]
            )
        )
    return out
