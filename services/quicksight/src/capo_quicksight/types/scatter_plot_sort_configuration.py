"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.items_limit_configuration


class ScatterPlotSortConfiguration(TypedDict, closed=True):
    scatter_plot_limit_configuration: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotSortConfiguration) -> dict:
    out: dict = {}
    if "scatter_plot_limit_configuration" in value:
        import capo_quicksight.types.items_limit_configuration

        out["ScatterPlotLimitConfiguration"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["scatter_plot_limit_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScatterPlotSortConfiguration:
    out: ScatterPlotSortConfiguration = {}  # type: ignore[typeddict-item]
    if "ScatterPlotLimitConfiguration" in data:
        import capo_quicksight.types.items_limit_configuration

        out["scatter_plot_limit_configuration"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["ScatterPlotLimitConfiguration"]
            )
        )
    return out
