"""Generated from Smithy shape ``com.amazonaws.appsync#ChannelNamespaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.channel_namespace

ChannelNamespaces: TypeAlias = list[
    "capo_appsync.types.channel_namespace.ChannelNamespace"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelNamespaces) -> list:
    import capo_appsync.types.channel_namespace

    out: list = []
    for item in value:
        out.append(capo_appsync.types.channel_namespace.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelNamespaces:
    import capo_appsync.types.channel_namespace

    out: ChannelNamespaces = []
    for item in data:
        out.append(capo_appsync.types.channel_namespace.deserialize_json(item))
    return out
