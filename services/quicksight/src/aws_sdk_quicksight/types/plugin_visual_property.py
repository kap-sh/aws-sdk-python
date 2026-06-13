"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualProperty``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class PluginVisualProperty(TypedDict):
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of the plugin visual property.</p>"""
    value: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The value of the plugin visual property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualProperty) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PluginVisualProperty:
    out: PluginVisualProperty = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
