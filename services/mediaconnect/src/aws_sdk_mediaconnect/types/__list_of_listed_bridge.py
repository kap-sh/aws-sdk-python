"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfListedBridge``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_bridge

__listOfListedBridge: TypeAlias = list[
    "aws_sdk_mediaconnect.types.listed_bridge.ListedBridge"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListedBridge) -> list:
    import aws_sdk_mediaconnect.types.listed_bridge

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.listed_bridge.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfListedBridge:
    import aws_sdk_mediaconnect.types.listed_bridge

    out: __listOfListedBridge = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.listed_bridge.deserialize_json(item))
    return out
