"""Generated from Smithy shape ``com.amazonaws.quicksight#SankeyDiagramFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sankey_diagram_aggregated_field_wells


class SankeyDiagramFieldWells(TypedDict, closed=True):
    sankey_diagram_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.sankey_diagram_aggregated_field_wells.SankeyDiagramAggregatedFieldWells"
    ]
    """<p>The field well configuration of a sankey diagram.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SankeyDiagramFieldWells) -> dict:
    out: dict = {}
    if "sankey_diagram_aggregated_field_wells" in value:
        import capo_quicksight.types.sankey_diagram_aggregated_field_wells

        out["SankeyDiagramAggregatedFieldWells"] = (
            capo_quicksight.types.sankey_diagram_aggregated_field_wells.serialize_json(
                value["sankey_diagram_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> SankeyDiagramFieldWells:
    out: SankeyDiagramFieldWells = {}  # type: ignore[typeddict-item]
    if "SankeyDiagramAggregatedFieldWells" in data:
        import capo_quicksight.types.sankey_diagram_aggregated_field_wells

        out["sankey_diagram_aggregated_field_wells"] = (
            capo_quicksight.types.sankey_diagram_aggregated_field_wells.deserialize_json(
                data["SankeyDiagramAggregatedFieldWells"]
            )
        )
    return out
