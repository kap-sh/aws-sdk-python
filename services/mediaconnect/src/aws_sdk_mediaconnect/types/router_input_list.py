"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input

RouterInputList: TypeAlias = list["aws_sdk_mediaconnect.types.router_input.RouterInput"]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputList) -> list:
    import aws_sdk_mediaconnect.types.router_input

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.router_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterInputList:
    import aws_sdk_mediaconnect.types.router_input

    out: RouterInputList = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.router_input.deserialize_json(item))
    return out
