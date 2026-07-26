"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.plugin_visual_property

PluginVisualPropertiesList: TypeAlias = list[
    "capo_quicksight.types.plugin_visual_property.PluginVisualProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualPropertiesList) -> list:
    import capo_quicksight.types.plugin_visual_property

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.plugin_visual_property.serialize_json(item))
    return out


def deserialize_json(data: list) -> PluginVisualPropertiesList:
    import capo_quicksight.types.plugin_visual_property

    out: PluginVisualPropertiesList = []
    for item in data:
        out.append(capo_quicksight.types.plugin_visual_property.deserialize_json(item))
    return out
