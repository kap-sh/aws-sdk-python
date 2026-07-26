"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualSortConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.plugin_visual_table_query_sort


class PluginVisualSortConfiguration(TypedDict, closed=True):
    plugin_visual_table_query_sort: NotRequired[
        "capo_quicksight.types.plugin_visual_table_query_sort.PluginVisualTableQuerySort"
    ]
    """<p>The table query sorting options for the plugin visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualSortConfiguration) -> dict:
    out: dict = {}
    if "plugin_visual_table_query_sort" in value:
        import capo_quicksight.types.plugin_visual_table_query_sort

        out["PluginVisualTableQuerySort"] = (
            capo_quicksight.types.plugin_visual_table_query_sort.serialize_json(
                value["plugin_visual_table_query_sort"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginVisualSortConfiguration:
    out: PluginVisualSortConfiguration = {}  # type: ignore[typeddict-item]
    if "PluginVisualTableQuerySort" in data:
        import capo_quicksight.types.plugin_visual_table_query_sort

        out["plugin_visual_table_query_sort"] = (
            capo_quicksight.types.plugin_visual_table_query_sort.deserialize_json(
                data["PluginVisualTableQuerySort"]
            )
        )
    return out
