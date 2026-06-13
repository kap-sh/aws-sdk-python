"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdatePluginRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.custom_plugin_configuration
    import aws_sdk_qbusiness.types.plugin_auth_configuration
    import aws_sdk_qbusiness.types.plugin_id
    import aws_sdk_qbusiness.types.plugin_name
    import aws_sdk_qbusiness.types.plugin_state
    import aws_sdk_qbusiness.types.url


class UpdatePluginRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application the plugin is attached to.</p>"""
    plugin_id: "aws_sdk_qbusiness.types.plugin_id.PluginId"
    """<p>The identifier of the plugin.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.plugin_name.PluginName"]
    """<p>The name of the plugin.</p>"""
    state: NotRequired["aws_sdk_qbusiness.types.plugin_state.PluginState"]
    """<p>The status of the plugin. </p>"""
    server_url: NotRequired["aws_sdk_qbusiness.types.url.Url"]
    """<p>The source URL used for plugin configuration.</p>"""
    custom_plugin_configuration: NotRequired[
        "aws_sdk_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
    ]
    """<p>The configuration for a custom plugin.</p>"""
    auth_configuration: NotRequired[
        "aws_sdk_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration"
    ]
    """<p>The authentication configuration the plugin is using.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePluginRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "state" in value:
        import aws_sdk_qbusiness.types.plugin_state

        out["state"] = aws_sdk_qbusiness.types.plugin_state.serialize_json(
            value["state"]
        )
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    if "custom_plugin_configuration" in value:
        import aws_sdk_qbusiness.types.custom_plugin_configuration

        out["customPluginConfiguration"] = (
            aws_sdk_qbusiness.types.custom_plugin_configuration.serialize_json(
                value["custom_plugin_configuration"]
            )
        )
    if "auth_configuration" in value:
        import aws_sdk_qbusiness.types.plugin_auth_configuration

        out["authConfiguration"] = (
            aws_sdk_qbusiness.types.plugin_auth_configuration.serialize_json(
                value["auth_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePluginRequest:
    out: UpdatePluginRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "state" in data:
        import aws_sdk_qbusiness.types.plugin_state

        out["state"] = aws_sdk_qbusiness.types.plugin_state.deserialize_json(
            data["state"]
        )
    if "serverUrl" in data:
        out["server_url"] = data["serverUrl"]
    if "customPluginConfiguration" in data:
        import aws_sdk_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            aws_sdk_qbusiness.types.custom_plugin_configuration.deserialize_json(
                data["customPluginConfiguration"]
            )
        )
    if "authConfiguration" in data:
        import aws_sdk_qbusiness.types.plugin_auth_configuration

        out["auth_configuration"] = (
            aws_sdk_qbusiness.types.plugin_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    return out
