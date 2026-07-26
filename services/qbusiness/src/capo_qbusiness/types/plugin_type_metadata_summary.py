"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginTypeMetadataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.plugin_type
    import capo_qbusiness.types.plugin_type_category
    import capo_qbusiness.types.string


class PluginTypeMetadataSummary(TypedDict, closed=True):
    type: NotRequired["capo_qbusiness.types.plugin_type.PluginType"]
    """<p>The type of the plugin.</p>"""
    category: NotRequired[
        "capo_qbusiness.types.plugin_type_category.PluginTypeCategory"
    ]
    """<p>The category of the plugin type.</p>"""
    description: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The description assigned by Amazon Q Business to a plugin. You can't modify this value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginTypeMetadataSummary) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_qbusiness.types.plugin_type

        out["type"] = capo_qbusiness.types.plugin_type.serialize_json(value["type"])
    if "category" in value:
        import capo_qbusiness.types.plugin_type_category

        out["category"] = capo_qbusiness.types.plugin_type_category.serialize_json(
            value["category"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PluginTypeMetadataSummary:
    out: PluginTypeMetadataSummary = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_qbusiness.types.plugin_type

        out["type"] = capo_qbusiness.types.plugin_type.deserialize_json(data["type"])
    if "category" in data:
        import capo_qbusiness.types.plugin_type_category

        out["category"] = capo_qbusiness.types.plugin_type_category.deserialize_json(
            data["category"]
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
