"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateChannelNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.auth_modes
    import aws_sdk_appsync.types.code
    import aws_sdk_appsync.types.handler_configs
    import aws_sdk_appsync.types.namespace
    import aws_sdk_appsync.types.string


class UpdateChannelNamespaceRequest(TypedDict):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The <code>Api</code> ID.</p>"""
    name: "aws_sdk_appsync.types.namespace.Namespace"
    """<p>The name of the <code>ChannelNamespace</code>.</p>"""
    subscribe_auth_modes: NotRequired["aws_sdk_appsync.types.auth_modes.AuthModes"]
    """<p>The authorization mode to use for subscribing to messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>"""
    publish_auth_modes: NotRequired["aws_sdk_appsync.types.auth_modes.AuthModes"]
    """<p>The authorization mode to use for publishing messages on the channel namespace. This configuration overrides the default <code>Api</code> authorization configuration.</p>"""
    code_handlers: NotRequired["aws_sdk_appsync.types.code.Code"]
    """<p>The event handler functions that run custom business logic to process published events and subscribe requests.</p>"""
    handler_configs: NotRequired["aws_sdk_appsync.types.handler_configs.HandlerConfigs"]
    """<p>The configuration for the <code>OnPublish</code> and <code>OnSubscribe</code> handlers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelNamespaceRequest) -> dict:
    out: dict = {}
    if "subscribe_auth_modes" in value:
        import aws_sdk_appsync.types.auth_modes

        out["subscribeAuthModes"] = aws_sdk_appsync.types.auth_modes.serialize_json(
            value["subscribe_auth_modes"]
        )
    if "publish_auth_modes" in value:
        import aws_sdk_appsync.types.auth_modes

        out["publishAuthModes"] = aws_sdk_appsync.types.auth_modes.serialize_json(
            value["publish_auth_modes"]
        )
    if "code_handlers" in value:
        out["codeHandlers"] = value["code_handlers"]
    if "handler_configs" in value:
        import aws_sdk_appsync.types.handler_configs

        out["handlerConfigs"] = aws_sdk_appsync.types.handler_configs.serialize_json(
            value["handler_configs"]
        )
    return out


def deserialize_json(data: dict) -> UpdateChannelNamespaceRequest:
    out: UpdateChannelNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "subscribeAuthModes" in data:
        import aws_sdk_appsync.types.auth_modes

        out["subscribe_auth_modes"] = aws_sdk_appsync.types.auth_modes.deserialize_json(
            data["subscribeAuthModes"]
        )
    if "publishAuthModes" in data:
        import aws_sdk_appsync.types.auth_modes

        out["publish_auth_modes"] = aws_sdk_appsync.types.auth_modes.deserialize_json(
            data["publishAuthModes"]
        )
    if "codeHandlers" in data:
        out["code_handlers"] = data["codeHandlers"]
    if "handlerConfigs" in data:
        import aws_sdk_appsync.types.handler_configs

        out["handler_configs"] = aws_sdk_appsync.types.handler_configs.deserialize_json(
            data["handlerConfigs"]
        )
    return out
