"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_message

RouterOutputMessages: TypeAlias = list[
    "capo_mediaconnect.types.router_output_message.RouterOutputMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputMessages) -> list:
    import capo_mediaconnect.types.router_output_message

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.router_output_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterOutputMessages:
    import capo_mediaconnect.types.router_output_message

    out: RouterOutputMessages = []
    for item in data:
        out.append(capo_mediaconnect.types.router_output_message.deserialize_json(item))
    return out
