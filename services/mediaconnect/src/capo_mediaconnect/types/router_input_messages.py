"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_message

RouterInputMessages: TypeAlias = list[
    "capo_mediaconnect.types.router_input_message.RouterInputMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputMessages) -> list:
    import capo_mediaconnect.types.router_input_message

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.router_input_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterInputMessages:
    import capo_mediaconnect.types.router_input_message

    out: RouterInputMessages = []
    for item in data:
        out.append(capo_mediaconnect.types.router_input_message.deserialize_json(item))
    return out
