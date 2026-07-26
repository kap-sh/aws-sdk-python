"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfBridgeSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_source

__listOfBridgeSource: TypeAlias = list[
    "capo_mediaconnect.types.bridge_source.BridgeSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBridgeSource) -> list:
    import capo_mediaconnect.types.bridge_source

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.bridge_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBridgeSource:
    import capo_mediaconnect.types.bridge_source

    out: __listOfBridgeSource = []
    for item in data:
        out.append(capo_mediaconnect.types.bridge_source.deserialize_json(item))
    return out
