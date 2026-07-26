"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfAddBridgeSourceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.add_bridge_source_request

__listOfAddBridgeSourceRequest: TypeAlias = list[
    "capo_mediaconnect.types.add_bridge_source_request.AddBridgeSourceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAddBridgeSourceRequest) -> list:
    import capo_mediaconnect.types.add_bridge_source_request

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.add_bridge_source_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAddBridgeSourceRequest:
    import capo_mediaconnect.types.add_bridge_source_request

    out: __listOfAddBridgeSourceRequest = []
    for item in data:
        out.append(
            capo_mediaconnect.types.add_bridge_source_request.deserialize_json(item)
        )
    return out
