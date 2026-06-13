"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.source

__listOfSource: TypeAlias = list["aws_sdk_mediaconnect.types.source.Source"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSource) -> list:
    import aws_sdk_mediaconnect.types.source

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSource:
    import aws_sdk_mediaconnect.types.source

    out: __listOfSource = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.source.deserialize_json(item))
    return out
