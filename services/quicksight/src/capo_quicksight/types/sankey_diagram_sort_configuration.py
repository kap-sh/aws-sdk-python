"""Generated from Smithy shape ``com.amazonaws.quicksight#SankeyDiagramSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_sort_options_list
    import capo_quicksight.types.items_limit_configuration


class SankeyDiagramSortConfiguration(TypedDict, closed=True):
    weight_sort: NotRequired[
        "capo_quicksight.types.field_sort_options_list.FieldSortOptionsList"
    ]
    """<p>The sort configuration of the weight fields.</p>"""
    source_items_limit: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of source nodes that are displayed in a sankey diagram.</p>"""
    destination_items_limit: NotRequired[
        "capo_quicksight.types.items_limit_configuration.ItemsLimitConfiguration"
    ]
    """<p>The limit on the number of destination nodes that are displayed in a sankey diagram.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SankeyDiagramSortConfiguration) -> dict:
    out: dict = {}
    if "weight_sort" in value:
        import capo_quicksight.types.field_sort_options_list

        out["WeightSort"] = (
            capo_quicksight.types.field_sort_options_list.serialize_json(
                value["weight_sort"]
            )
        )
    if "source_items_limit" in value:
        import capo_quicksight.types.items_limit_configuration

        out["SourceItemsLimit"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["source_items_limit"]
            )
        )
    if "destination_items_limit" in value:
        import capo_quicksight.types.items_limit_configuration

        out["DestinationItemsLimit"] = (
            capo_quicksight.types.items_limit_configuration.serialize_json(
                value["destination_items_limit"]
            )
        )
    return out


def deserialize_json(data: dict) -> SankeyDiagramSortConfiguration:
    out: SankeyDiagramSortConfiguration = {}  # type: ignore[typeddict-item]
    if "WeightSort" in data:
        import capo_quicksight.types.field_sort_options_list

        out["weight_sort"] = (
            capo_quicksight.types.field_sort_options_list.deserialize_json(
                data["WeightSort"]
            )
        )
    if "SourceItemsLimit" in data:
        import capo_quicksight.types.items_limit_configuration

        out["source_items_limit"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["SourceItemsLimit"]
            )
        )
    if "DestinationItemsLimit" in data:
        import capo_quicksight.types.items_limit_configuration

        out["destination_items_limit"] = (
            capo_quicksight.types.items_limit_configuration.deserialize_json(
                data["DestinationItemsLimit"]
            )
        )
    return out
