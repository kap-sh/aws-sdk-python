"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#Uris``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_signaling.types.uri

Uris: TypeAlias = list["aws_sdk_kinesis_video_signaling.types.uri.Uri"]


# --- restJson1 ser/de ---
def serialize_json(value: Uris) -> list:
    return list(value)


def deserialize_json(data: list) -> Uris:
    return list(data)
