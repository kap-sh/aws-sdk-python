"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_filter

RouterOutputFilterList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.router_output_filter.RouterOutputFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputFilterList) -> list:
    import aws_sdk_mediaconnect.types.router_output_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.router_output_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouterOutputFilterList:
    import aws_sdk_mediaconnect.types.router_output_filter

    out: RouterOutputFilterList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.router_output_filter.deserialize_json(item)
        )
    return out
