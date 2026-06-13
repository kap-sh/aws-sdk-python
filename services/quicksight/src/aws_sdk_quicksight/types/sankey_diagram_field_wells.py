"""Generated from Smithy shape ``com.amazonaws.quicksight#SankeyDiagramFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sankey_diagram_aggregated_field_wells


class SankeyDiagramFieldWells(TypedDict):
    sankey_diagram_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.sankey_diagram_aggregated_field_wells.SankeyDiagramAggregatedFieldWells"
    ]
    """<p>The field well configuration of a sankey diagram.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SankeyDiagramFieldWells) -> dict:
    out: dict = {}
    if "sankey_diagram_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.sankey_diagram_aggregated_field_wells

        out["SankeyDiagramAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.sankey_diagram_aggregated_field_wells.serialize_json(
                value["sankey_diagram_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> SankeyDiagramFieldWells:
    out: SankeyDiagramFieldWells = {}  # type: ignore[typeddict-item]
    if "SankeyDiagramAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.sankey_diagram_aggregated_field_wells

        out["sankey_diagram_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.sankey_diagram_aggregated_field_wells.deserialize_json(
                data["SankeyDiagramAggregatedFieldWells"]
            )
        )
    return out
