"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.scatter_plot_categorically_aggregated_field_wells
    import aws_sdk_quicksight.types.scatter_plot_unaggregated_field_wells


class ScatterPlotFieldWells(TypedDict):
    scatter_plot_categorically_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.scatter_plot_categorically_aggregated_field_wells.ScatterPlotCategoricallyAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a scatter plot. The x and y-axes of scatter plots with aggregated field wells are aggregated by category, label, or both.</p>"""
    scatter_plot_unaggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.scatter_plot_unaggregated_field_wells.ScatterPlotUnaggregatedFieldWells"
    ]
    """<p>The unaggregated field wells of a scatter plot. The x and y-axes of these scatter plots are unaggregated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotFieldWells) -> dict:
    out: dict = {}
    if "scatter_plot_categorically_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.scatter_plot_categorically_aggregated_field_wells

        out["ScatterPlotCategoricallyAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.scatter_plot_categorically_aggregated_field_wells.serialize_json(
                value["scatter_plot_categorically_aggregated_field_wells"]
            )
        )
    if "scatter_plot_unaggregated_field_wells" in value:
        import aws_sdk_quicksight.types.scatter_plot_unaggregated_field_wells

        out["ScatterPlotUnaggregatedFieldWells"] = (
            aws_sdk_quicksight.types.scatter_plot_unaggregated_field_wells.serialize_json(
                value["scatter_plot_unaggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScatterPlotFieldWells:
    out: ScatterPlotFieldWells = {}  # type: ignore[typeddict-item]
    if "ScatterPlotCategoricallyAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.scatter_plot_categorically_aggregated_field_wells

        out["scatter_plot_categorically_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.scatter_plot_categorically_aggregated_field_wells.deserialize_json(
                data["ScatterPlotCategoricallyAggregatedFieldWells"]
            )
        )
    if "ScatterPlotUnaggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.scatter_plot_unaggregated_field_wells

        out["scatter_plot_unaggregated_field_wells"] = (
            aws_sdk_quicksight.types.scatter_plot_unaggregated_field_wells.deserialize_json(
                data["ScatterPlotUnaggregatedFieldWells"]
            )
        )
    return out
