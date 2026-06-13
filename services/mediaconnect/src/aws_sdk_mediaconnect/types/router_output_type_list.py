"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_type

RouterOutputTypeList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.router_output_type.RouterOutputType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputTypeList) -> list:
    import aws_sdk_mediaconnect.types.router_output_type

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.router_output_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterOutputTypeList:
    import aws_sdk_mediaconnect.types.router_output_type

    out: RouterOutputTypeList = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.router_output_type.deserialize_json(item))
    return out
