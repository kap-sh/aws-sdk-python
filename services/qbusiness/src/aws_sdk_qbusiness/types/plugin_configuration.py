"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.plugin_id


class PluginConfiguration(TypedDict, closed=True):
    plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId"
    """<p> The identifier of the plugin you want to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginConfiguration) -> dict:
    out: dict = {}
    out["pluginId"] = value["plugin_id"]
    return out


def deserialize_json(data: dict) -> PluginConfiguration:
    out: PluginConfiguration = {}  # type: ignore[typeddict-item]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    else:
        raise DeserializationError("PluginConfiguration.plugin_id required")
    return out
