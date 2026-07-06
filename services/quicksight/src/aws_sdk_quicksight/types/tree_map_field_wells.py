"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.tree_map_aggregated_field_wells


class TreeMapFieldWells(TypedDict, closed=True):
    tree_map_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.tree_map_aggregated_field_wells.TreeMapAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a tree map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapFieldWells) -> dict:
    out: dict = {}
    if "tree_map_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.tree_map_aggregated_field_wells

        out["TreeMapAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.tree_map_aggregated_field_wells.serialize_json(
                value["tree_map_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> TreeMapFieldWells:
    out: TreeMapFieldWells = {}  # type: ignore[typeddict-item]
    if "TreeMapAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.tree_map_aggregated_field_wells

        out["tree_map_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.tree_map_aggregated_field_wells.deserialize_json(
                data["TreeMapAggregatedFieldWells"]
            )
        )
    return out
