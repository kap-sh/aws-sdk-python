"""Generated from Smithy shape ``com.amazonaws.connect#MediaConcurrencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.media_concurrency

MediaConcurrencies: TypeAlias = list[
    "aws_sdk_connect.types.media_concurrency.MediaConcurrency"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaConcurrencies) -> list:
    import aws_sdk_connect.types.media_concurrency

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.media_concurrency.serialize_json(item))
    return out


def deserialize_json(data: list) -> MediaConcurrencies:
    import aws_sdk_connect.types.media_concurrency

    out: MediaConcurrencies = []
    for item in data:
        out.append(aws_sdk_connect.types.media_concurrency.deserialize_json(item))
    return out
