"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.plugin_visual_properties_list


class PluginVisualOptions(TypedDict, closed=True):
    visual_properties: NotRequired[
        "capo_quicksight.types.plugin_visual_properties_list.PluginVisualPropertiesList"
    ]
    """<p>The persisted properties and their values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualOptions) -> dict:
    out: dict = {}
    if "visual_properties" in value:
        import capo_quicksight.types.plugin_visual_properties_list

        out["VisualProperties"] = (
            capo_quicksight.types.plugin_visual_properties_list.serialize_json(
                value["visual_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginVisualOptions:
    out: PluginVisualOptions = {}  # type: ignore[typeddict-item]
    if "VisualProperties" in data:
        import capo_quicksight.types.plugin_visual_properties_list

        out["visual_properties"] = (
            capo_quicksight.types.plugin_visual_properties_list.deserialize_json(
                data["VisualProperties"]
            )
        )
    return out
