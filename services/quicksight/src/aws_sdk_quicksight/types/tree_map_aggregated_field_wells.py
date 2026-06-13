"""Generated from Smithy shape ``com.amazonaws.quicksight#TreeMapAggregatedFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.tree_map_dimension_field_list
    import aws_sdk_quicksight.types.tree_map_measure_field_list


class TreeMapAggregatedFieldWells(TypedDict):
    groups: NotRequired[
        "aws_sdk_quicksight.types.tree_map_dimension_field_list.TreeMapDimensionFieldList"
    ]
    """<p>The group by field well of a tree map. Values are grouped based on group by fields.</p>"""
    sizes: NotRequired[
        "aws_sdk_quicksight.types.tree_map_measure_field_list.TreeMapMeasureFieldList"
    ]
    """<p>The size field well of a tree map. Values are aggregated based on group by fields.</p>"""
    colors: NotRequired[
        "aws_sdk_quicksight.types.tree_map_measure_field_list.TreeMapMeasureFieldList"
    ]
    """<p>The color field well of a tree map. Values are grouped by aggregations based on group by fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TreeMapAggregatedFieldWells) -> dict:
    out: dict = {}
    if "groups" in value:
        import aws_sdk_quicksight.types.tree_map_dimension_field_list

        out["Groups"] = (
            aws_sdk_quicksight.types.tree_map_dimension_field_list.serialize_json(
                value["groups"]
            )
        )
    if "sizes" in value:
        import aws_sdk_quicksight.types.tree_map_measure_field_list

        out["Sizes"] = (
            aws_sdk_quicksight.types.tree_map_measure_field_list.serialize_json(
                value["sizes"]
            )
        )
    if "colors" in value:
        import aws_sdk_quicksight.types.tree_map_measure_field_list

        out["Colors"] = (
            aws_sdk_quicksight.types.tree_map_measure_field_list.serialize_json(
                value["colors"]
            )
        )
    return out


def deserialize_json(data: dict) -> TreeMapAggregatedFieldWells:
    out: TreeMapAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import aws_sdk_quicksight.types.tree_map_dimension_field_list

        out["groups"] = (
            aws_sdk_quicksight.types.tree_map_dimension_field_list.deserialize_json(
                data["Groups"]
            )
        )
    if "Sizes" in data:
        import aws_sdk_quicksight.types.tree_map_measure_field_list

        out["sizes"] = (
            aws_sdk_quicksight.types.tree_map_measure_field_list.deserialize_json(
                data["Sizes"]
            )
        )
    if "Colors" in data:
        import aws_sdk_quicksight.types.tree_map_measure_field_list

        out["colors"] = (
            aws_sdk_quicksight.types.tree_map_measure_field_list.deserialize_json(
                data["Colors"]
            )
        )
    return out
