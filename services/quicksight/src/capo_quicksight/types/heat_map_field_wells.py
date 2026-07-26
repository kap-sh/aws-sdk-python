"""Generated from Smithy shape ``com.amazonaws.quicksight#HeatMapFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.heat_map_aggregated_field_wells


class HeatMapFieldWells(TypedDict, closed=True):
    heat_map_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.heat_map_aggregated_field_wells.HeatMapAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a heat map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeatMapFieldWells) -> dict:
    out: dict = {}
    if "heat_map_aggregated_field_wells" in value:
        import capo_quicksight.types.heat_map_aggregated_field_wells

        out["HeatMapAggregatedFieldWells"] = (
            capo_quicksight.types.heat_map_aggregated_field_wells.serialize_json(
                value["heat_map_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> HeatMapFieldWells:
    out: HeatMapFieldWells = {}  # type: ignore[typeddict-item]
    if "HeatMapAggregatedFieldWells" in data:
        import capo_quicksight.types.heat_map_aggregated_field_wells

        out["heat_map_aggregated_field_wells"] = (
            capo_quicksight.types.heat_map_aggregated_field_wells.deserialize_json(
                data["HeatMapAggregatedFieldWells"]
            )
        )
    return out
