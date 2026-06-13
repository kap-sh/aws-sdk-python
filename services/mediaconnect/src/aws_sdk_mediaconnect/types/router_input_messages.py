"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_message

RouterInputMessages: TypeAlias = list[
    "aws_sdk_mediaconnect.types.router_input_message.RouterInputMessage"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputMessages) -> list:
    import aws_sdk_mediaconnect.types.router_input_message

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.router_input_message.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterInputMessages:
    import aws_sdk_mediaconnect.types.router_input_message

    out: RouterInputMessages = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.router_input_message.deserialize_json(item)
        )
    return out
