"""Generated from Smithy shape ``com.amazonaws.appsync#HandlerConfigs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appsync.types.handler_config


class HandlerConfigs(TypedDict, closed=True):
    on_publish: NotRequired["aws_sdk_appsync.types.handler_config.HandlerConfig"]
    """<p>The configuration for the <code>OnPublish</code> handler.</p>"""
    on_subscribe: NotRequired["aws_sdk_appsync.types.handler_config.HandlerConfig"]
    """<p>The configuration for the <code>OnSubscribe</code> handler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HandlerConfigs) -> dict:
    out: dict = {}
    if "on_publish" in value:
        import aws_sdk_appsync.types.handler_config

        out["onPublish"] = aws_sdk_appsync.types.handler_config.serialize_json(
            value["on_publish"]
        )
    if "on_subscribe" in value:
        import aws_sdk_appsync.types.handler_config

        out["onSubscribe"] = aws_sdk_appsync.types.handler_config.serialize_json(
            value["on_subscribe"]
        )
    return out


def deserialize_json(data: dict) -> HandlerConfigs:
    out: HandlerConfigs = {}  # type: ignore[typeddict-item]
    if "onPublish" in data:
        import aws_sdk_appsync.types.handler_config

        out["on_publish"] = aws_sdk_appsync.types.handler_config.deserialize_json(
            data["onPublish"]
        )
    if "onSubscribe" in data:
        import aws_sdk_appsync.types.handler_config

        out["on_subscribe"] = aws_sdk_appsync.types.handler_config.deserialize_json(
            data["onSubscribe"]
        )
    return out
