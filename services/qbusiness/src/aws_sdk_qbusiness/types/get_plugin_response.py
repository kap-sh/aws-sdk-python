"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetPluginResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.custom_plugin_configuration
    import aws_sdk_qbusiness.types.plugin_arn
    import aws_sdk_qbusiness.types.plugin_auth_configuration
    import aws_sdk_qbusiness.types.plugin_build_status
    import aws_sdk_qbusiness.types.plugin_id
    import aws_sdk_qbusiness.types.plugin_name
    import aws_sdk_qbusiness.types.plugin_state
    import aws_sdk_qbusiness.types.plugin_type
    import aws_sdk_qbusiness.types.timestamp
    import aws_sdk_qbusiness.types.url


class GetPluginResponse(TypedDict):
    application_id: NotRequired["aws_sdk_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the application which contains the plugin.</p>"""
    plugin_id: NotRequired["aws_sdk_qbusiness.types.plugin_id.PluginId"]
    """<p>The identifier of the plugin.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.plugin_name.PluginName"]
    """<p>The name of the plugin.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.plugin_type.PluginType"]
    """<p>The type of the plugin.</p>"""
    server_url: NotRequired["aws_sdk_qbusiness.types.url.Url"]
    """<p>The source URL used for plugin configuration.</p>"""
    auth_configuration: NotRequired[
        "aws_sdk_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration"
    ]
    custom_plugin_configuration: NotRequired[
        "aws_sdk_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
    ]
    """<p>Configuration information required to create a custom plugin.</p>"""
    build_status: NotRequired[
        "aws_sdk_qbusiness.types.plugin_build_status.PluginBuildStatus"
    ]
    """<p>The current status of a plugin. A plugin is modified asynchronously.</p>"""
    plugin_arn: NotRequired["aws_sdk_qbusiness.types.plugin_arn.PluginArn"]
    """<p>The Amazon Resource Name (ARN) of the role with permission to access resources needed to create the plugin.</p>"""
    state: NotRequired["aws_sdk_qbusiness.types.plugin_state.PluginState"]
    """<p>The current state of the plugin.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the plugin was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp for when the plugin was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPluginResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "plugin_id" in value:
        out["pluginId"] = value["plugin_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "type" in value:
        import aws_sdk_qbusiness.types.plugin_type

        out["type"] = aws_sdk_qbusiness.types.plugin_type.serialize_json(value["type"])
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    if "auth_configuration" in value:
        import aws_sdk_qbusiness.types.plugin_auth_configuration

        out["authConfiguration"] = (
            aws_sdk_qbusiness.types.plugin_auth_configuration.serialize_json(
                value["auth_configuration"]
            )
        )
    if "custom_plugin_configuration" in value:
        import aws_sdk_qbusiness.types.custom_plugin_configuration

        out["customPluginConfiguration"] = (
            aws_sdk_qbusiness.types.custom_plugin_configuration.serialize_json(
                value["custom_plugin_configuration"]
            )
        )
    if "build_status" in value:
        import aws_sdk_qbusiness.types.plugin_build_status

        out["buildStatus"] = aws_sdk_qbusiness.types.plugin_build_status.serialize_json(
            value["build_status"]
        )
    if "plugin_arn" in value:
        out["pluginArn"] = value["plugin_arn"]
    if "state" in value:
        import aws_sdk_qbusiness.types.plugin_state

        out["state"] = aws_sdk_qbusiness.types.plugin_state.serialize_json(
            value["state"]
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


def deserialize_json(data: dict) -> GetPluginResponse:
    out: GetPluginResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "pluginId" in data:
        out["plugin_id"] = data["pluginId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "type" in data:
        import aws_sdk_qbusiness.types.plugin_type

        out["type"] = aws_sdk_qbusiness.types.plugin_type.deserialize_json(data["type"])
    if "serverUrl" in data:
        out["server_url"] = data["serverUrl"]
    if "authConfiguration" in data:
        import aws_sdk_qbusiness.types.plugin_auth_configuration

        out["auth_configuration"] = (
            aws_sdk_qbusiness.types.plugin_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    if "customPluginConfiguration" in data:
        import aws_sdk_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            aws_sdk_qbusiness.types.custom_plugin_configuration.deserialize_json(
                data["customPluginConfiguration"]
            )
        )
    if "buildStatus" in data:
        import aws_sdk_qbusiness.types.plugin_build_status

        out["build_status"] = (
            aws_sdk_qbusiness.types.plugin_build_status.deserialize_json(
                data["buildStatus"]
            )
        )
    if "pluginArn" in data:
        out["plugin_arn"] = data["pluginArn"]
    if "state" in data:
        import aws_sdk_qbusiness.types.plugin_state

        out["state"] = aws_sdk_qbusiness.types.plugin_state.deserialize_json(
            data["state"]
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
