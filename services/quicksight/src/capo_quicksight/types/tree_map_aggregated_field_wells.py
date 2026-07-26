"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.tree_map_dimension_field_list
    import capo_quicksight.types.tree_map_measure_field_list


class TreeMapAggregatedFieldWells(TypedDict, closed=True):
    groups: NotRequired[
        "capo_quicksight.types.tree_map_dimension_field_list.TreeMapDimensionFieldList"
    ]
    """<p>The group by field well of a tree map. Values are grouped based on group by fields.</p>"""
    sizes: NotRequired[
        "capo_quicksight.types.tree_map_measure_field_list.TreeMapMeasureFieldList"
    ]
    """<p>The size field well of a tree map. Values are aggregated based on group by fields.</p>"""
    colors: NotRequired[
        "capo_quicksight.types.tree_map_measure_field_list.TreeMapMeasureFieldList"
    ]
    """<p>The color field well of a tree map. Values are grouped by aggregations based on group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapAggregatedFieldWells) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_quicksight.types.tree_map_dimension_field_list

        out["Groups"] = (
            capo_quicksight.types.tree_map_dimension_field_list.serialize_json(
                value["groups"]
            )
        )
    if "sizes" in value:
        import capo_quicksight.types.tree_map_measure_field_list

        out["Sizes"] = capo_quicksight.types.tree_map_measure_field_list.serialize_json(
            value["sizes"]
        )
    if "colors" in value:
        import capo_quicksight.types.tree_map_measure_field_list

        out["Colors"] = (
            capo_quicksight.types.tree_map_measure_field_list.serialize_json(
                value["colors"]
            )
        )
    return out


def deserialize_json(data: dict) -> TreeMapAggregatedFieldWells:
    out: TreeMapAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import capo_quicksight.types.tree_map_dimension_field_list

        out["groups"] = (
            capo_quicksight.types.tree_map_dimension_field_list.deserialize_json(
                data["Groups"]
            )
        )
    if "Sizes" in data:
        import capo_quicksight.types.tree_map_measure_field_list

        out["sizes"] = (
            capo_quicksight.types.tree_map_measure_field_list.deserialize_json(
                data["Sizes"]
            )
        )
    if "Colors" in data:
        import capo_quicksight.types.tree_map_measure_field_list

        out["colors"] = (
            capo_quicksight.types.tree_map_measure_field_list.deserialize_json(
                data["Colors"]
            )
        )
    return out
