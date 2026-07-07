"""Generated from Smithy shape ``com.amazonaws.qbusiness#Plugin``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.plugin_build_status
    import aws_sdk_qbusiness.types.plugin_id
    import aws_sdk_qbusiness.types.plugin_name
    import aws_sdk_qbusiness.types.plugin_state
    import aws_sdk_qbusiness.types.plugin_type
    import aws_sdk_qbusiness.types.timestamp
    import aws_sdk_qbusiness.types.url


class Plugin(TypedDict, closed=True):
    plugin_id: NotRequired["aws_sdk_qbusiness.types.plugin_id.PluginId"]
    """<p>The identifier of the plugin.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.plugin_name.PluginName"]
    """<p>The name of the plugin.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.plugin_type.PluginType"]
    """<p>The type of the plugin.</p>"""
    server_url: NotRequired["aws_sdk_qbusiness.types.url.Url"]
    """<p>The plugin server URL used for configuration.</p>"""
    state: NotRequired["aws_sdk_qbusiness.types.plugin_state.PluginState"]
    """<p>The current status of the plugin.</p>"""
    build_status: NotRequired[
        "aws_sdk_qbusiness.types.plugin_build_status.PluginBuildStatus"
    ]
    """<p>The status of the plugin.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the plugin was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the plugin was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Plugin) -> dict:
    out: dict = {}
    if "plugin_id" in value:
        out["pluginId"] = value["plugin_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "type" in value:
        import aws_sdk_qbusiness.types.plugin_type

        out["type"] = aws_sdk_qbusiness.types.plugin_type.serialize_json(value["type"])
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    if "state" in value:
        import aws_sdk_qbusiness.types.plugin_state

        out["state"] = aws_sdk_qbusiness.types.plugin_state.serialize_json(
            value["state"]
        )
    if "build_status" in value:
        import aws_sdk_qbusiness.types.plugin_build_status

        out["buildStatus"] = aws_sdk_qbusiness.types.plugin_build_status.serialize_json(
            value["build_status"]
        )
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Plugin:
    out: Plugin = {}  # type: ignore[typeddict-item]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "type" in data:
        import aws_sdk_qbusiness.types.plugin_type

        out["type"] = aws_sdk_qbusiness.types.plugin_type.deserialize_json(data["type"])
    if "serverUrl" in data:
        out["server_url"] = data["serverUrl"]
    if "state" in data:
        import aws_sdk_qbusiness.types.plugin_state

        out["state"] = aws_sdk_qbusiness.types.plugin_state.deserialize_json(
            data["state"]
        )
    if "buildStatus" in data:
        import aws_sdk_qbusiness.types.plugin_build_status

        out["build_status"] = (
            aws_sdk_qbusiness.types.plugin_build_status.deserialize_json(
                data["buildStatus"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
