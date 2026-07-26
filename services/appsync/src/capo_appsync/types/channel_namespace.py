"""Generated from Smithy shape ``com.amazonaws.appsync#ChannelNamespace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.auth_modes
    import capo_appsync.types.code
    import capo_appsync.types.handler_configs
    import capo_appsync.types.namespace
    import capo_appsync.types.string
    import capo_appsync.types.tag_map
    import capo_appsync.types.timestamp


class ChannelNamespace(TypedDict, closed=True):
    api_id: NotRequired["capo_appsync.types.string.String"]
    """<p>The <code>Api</code> ID.</p>"""
    name: NotRequired["capo_appsync.types.namespace.Namespace"]
    """<p>The name of the channel namespace. This name must be unique within the <code>Api</code>.</p>"""
    subscribe_auth_modes: NotRequired["capo_appsync.types.auth_modes.AuthModes"]
    """<p>The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default <code>Api</code>authorization configuration.</p>"""
    publish_auth_modes: NotRequired["capo_appsync.types.auth_modes.AuthModes"]
    """<p>The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default <code>Api</code>authorization configuration.</p>"""
    code_handlers: NotRequired["capo_appsync.types.code.Code"]
    """<p>The event handler functions that run custom business logic to process published events and subscribe requests.</p>"""
    tags: NotRequired["capo_appsync.types.tag_map.TagMap"]
    channel_namespace_arn: NotRequired["capo_appsync.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the <code>ChannelNamespace</code>.</p>"""
    created: NotRequired["capo_appsync.types.timestamp.Timestamp"]
    """<p>The date and time that the <code>ChannelNamespace</code> was created.</p>"""
    last_modified: NotRequired["capo_appsync.types.timestamp.Timestamp"]
    """<p>The date and time that the <code>ChannelNamespace</code> was last changed.</p>"""
    handler_configs: NotRequired["capo_appsync.types.handler_configs.HandlerConfigs"]
    """<p>The configuration for the <code>OnPublish</code> and <code>OnSubscribe</code> handlers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelNamespace) -> dict:
    out: dict = {}
    if "api_id" in value:
        out["apiId"] = value["api_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "subscribe_auth_modes" in value:
        import capo_appsync.types.auth_modes

        out["subscribeAuthModes"] = capo_appsync.types.auth_modes.serialize_json(
            value["subscribe_auth_modes"]
        )
    if "publish_auth_modes" in value:
        import capo_appsync.types.auth_modes

        out["publishAuthModes"] = capo_appsync.types.auth_modes.serialize_json(
            value["publish_auth_modes"]
        )
    if "code_handlers" in value:
        out["codeHandlers"] = value["code_handlers"]
    if "tags" in value:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.serialize_json(value["tags"])
    if "channel_namespace_arn" in value:
        out["channelNamespaceArn"] = value["channel_namespace_arn"]
    if "created" in value:
        import capo_appsync.types.timestamp

        out["created"] = capo_appsync.types.timestamp.serialize_json(value["created"])
    if "last_modified" in value:
        import capo_appsync.types.timestamp

        out["lastModified"] = capo_appsync.types.timestamp.serialize_json(
            value["last_modified"]
        )
    if "handler_configs" in value:
        import capo_appsync.types.handler_configs

        out["handlerConfigs"] = capo_appsync.types.handler_configs.serialize_json(
            value["handler_configs"]
        )
    return out


def deserialize_json(data: dict) -> ChannelNamespace:
    out: ChannelNamespace = {}  # type: ignore[typeddict-item]
    if "apiId" in data:
        out["api_id"] = data["apiId"]
    if "name" in data:
        out["name"] = data["name"]
    if "subscribeAuthModes" in data:
        import capo_appsync.types.auth_modes

        out["subscribe_auth_modes"] = capo_appsync.types.auth_modes.deserialize_json(
            data["subscribeAuthModes"]
        )
    if "publishAuthModes" in data:
        import capo_appsync.types.auth_modes

        out["publish_auth_modes"] = capo_appsync.types.auth_modes.deserialize_json(
            data["publishAuthModes"]
        )
    if "codeHandlers" in data:
        out["code_handlers"] = data["codeHandlers"]
    if "tags" in data:
        import capo_appsync.types.tag_map

        out["tags"] = capo_appsync.types.tag_map.deserialize_json(data["tags"])
    if "channelNamespaceArn" in data:
        out["channel_namespace_arn"] = data["channelNamespaceArn"]
    if "created" in data:
        import capo_appsync.types.timestamp

        out["created"] = capo_appsync.types.timestamp.deserialize_json(data["created"])
    if "lastModified" in data:
        import capo_appsync.types.timestamp

        out["last_modified"] = capo_appsync.types.timestamp.deserialize_json(
            data["lastModified"]
        )
    if "handlerConfigs" in data:
        import capo_appsync.types.handler_configs

        out["handler_configs"] = capo_appsync.types.handler_configs.deserialize_json(
            data["handlerConfigs"]
        )
    return out
