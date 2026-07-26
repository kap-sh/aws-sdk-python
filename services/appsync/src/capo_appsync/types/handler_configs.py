"""Generated from Smithy shape ``com.amazonaws.appsync#HandlerConfigs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.handler_config


class HandlerConfigs(TypedDict, closed=True):
    on_publish: NotRequired["capo_appsync.types.handler_config.HandlerConfig"]
    """<p>The configuration for the <code>OnPublish</code> handler.</p>"""
    on_subscribe: NotRequired["capo_appsync.types.handler_config.HandlerConfig"]
    """<p>The configuration for the <code>OnSubscribe</code> handler.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HandlerConfigs) -> dict:
    out: dict = {}
    if "on_publish" in value:
        import capo_appsync.types.handler_config

        out["onPublish"] = capo_appsync.types.handler_config.serialize_json(
            value["on_publish"]
        )
    if "on_subscribe" in value:
        import capo_appsync.types.handler_config

        out["onSubscribe"] = capo_appsync.types.handler_config.serialize_json(
            value["on_subscribe"]
        )
    return out


def deserialize_json(data: dict) -> HandlerConfigs:
    out: HandlerConfigs = {}  # type: ignore[typeddict-item]
    if "onPublish" in data:
        import capo_appsync.types.handler_config

        out["on_publish"] = capo_appsync.types.handler_config.deserialize_json(
            data["onPublish"]
        )
    if "onSubscribe" in data:
        import capo_appsync.types.handler_config

        out["on_subscribe"] = capo_appsync.types.handler_config.deserialize_json(
            data["onSubscribe"]
        )
    return out
