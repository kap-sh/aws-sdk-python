"""Generated from Smithy shape ``com.amazonaws.opensearch#PluginProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.plugin_class_name
    import aws_sdk_opensearch.types.plugin_description
    import aws_sdk_opensearch.types.plugin_name
    import aws_sdk_opensearch.types.plugin_version
    import aws_sdk_opensearch.types.uncompressed_plugin_size_in_bytes


class PluginProperties(TypedDict):
    name: NotRequired["aws_sdk_opensearch.types.plugin_name.PluginName"]
    """<p>The name of the plugin.</p>"""
    description: NotRequired[
        "aws_sdk_opensearch.types.plugin_description.PluginDescription"
    ]
    """<p>The description of the plugin.</p>"""
    version: NotRequired["aws_sdk_opensearch.types.plugin_version.PluginVersion"]
    """<p>The version of the plugin.</p>"""
    class_name: NotRequired[
        "aws_sdk_opensearch.types.plugin_class_name.PluginClassName"
    ]
    """<p>The name of the class to load.</p>"""
    uncompressed_size_in_bytes: NotRequired[
        "aws_sdk_opensearch.types.uncompressed_plugin_size_in_bytes.UncompressedPluginSizeInBytes"
    ]
    """<p>The uncompressed size of the plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginProperties) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "version" in value:
        out["Version"] = value["version"]
    if "class_name" in value:
        out["ClassName"] = value["class_name"]
    if "uncompressed_size_in_bytes" in value:
        out["UncompressedSizeInBytes"] = value["uncompressed_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> PluginProperties:
    out: PluginProperties = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "ClassName" in data:
        out["class_name"] = data["ClassName"]
    if "UncompressedSizeInBytes" in data:
        out["uncompressed_size_in_bytes"] = data["UncompressedSizeInBytes"]
    return out
