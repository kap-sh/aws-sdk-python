"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreatePluginRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.custom_plugin_configuration
    import aws_sdk_qbusiness.types.plugin_auth_configuration
    import aws_sdk_qbusiness.types.plugin_name
    import aws_sdk_qbusiness.types.plugin_type
    import aws_sdk_qbusiness.types.tags
    import aws_sdk_qbusiness.types.url


class CreatePluginRequest(TypedDict):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application that will contain the plugin.</p>"""
    display_name: "aws_sdk_qbusiness.types.plugin_name.PluginName"
    """<p>A the name for your plugin.</p>"""
    type: "aws_sdk_qbusiness.types.plugin_type.PluginType"
    """<p>The type of plugin you want to create.</p>"""
    auth_configuration: (
        "aws_sdk_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration"
    )
    server_url: NotRequired["aws_sdk_qbusiness.types.url.Url"]
    """<p>The source URL used for plugin configuration.</p>"""
    custom_plugin_configuration: NotRequired[
        "aws_sdk_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
    ]
    """<p>Contains configuration for a custom plugin.</p>"""
    tags: NotRequired["aws_sdk_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create your Amazon Q Business plugin.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePluginRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    import aws_sdk_qbusiness.types.plugin_type

    out["type"] = aws_sdk_qbusiness.types.plugin_type.serialize_json(value["type"])
    import aws_sdk_qbusiness.types.plugin_auth_configuration

    out["authConfiguration"] = (
        aws_sdk_qbusiness.types.plugin_auth_configuration.serialize_json(
            value["auth_configuration"]
        )
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
    if "tags" in value:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePluginRequest:
    out: CreatePluginRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreatePluginRequest.display_name required")
    if "type" in data:
        import aws_sdk_qbusiness.types.plugin_type

        out["type"] = aws_sdk_qbusiness.types.plugin_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("CreatePluginRequest.type required")
    if "authConfiguration" in data:
        import aws_sdk_qbusiness.types.plugin_auth_configuration

        out["auth_configuration"] = (
            aws_sdk_qbusiness.types.plugin_auth_configuration.deserialize_json(
                data["authConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreatePluginRequest.auth_configuration required")
    if "serverUrl" in data:
        out["server_url"] = data["serverUrl"]
    if "customPluginConfiguration" in data:
        import aws_sdk_qbusiness.types.custom_plugin_configuration

        out["custom_plugin_configuration"] = (
            aws_sdk_qbusiness.types.custom_plugin_configuration.deserialize_json(
                data["customPluginConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
