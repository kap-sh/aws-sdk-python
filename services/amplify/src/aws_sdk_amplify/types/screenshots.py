"""Generated from Smithy shape ``com.amazonaws.amplify#Screenshots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplify.types.thumbnail_name
    import aws_sdk_amplify.types.thumbnail_url

Screenshots: TypeAlias = dict[
    "aws_sdk_amplify.types.thumbnail_name.ThumbnailName",
    "aws_sdk_amplify.types.thumbnail_url.ThumbnailUrl",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Screenshots) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Screenshots:
    out: Screenshots = {}
    for key, value in data.items():
        out[key] = value
    return out
