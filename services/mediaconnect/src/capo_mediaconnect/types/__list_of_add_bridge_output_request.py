"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfAddBridgeOutputRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.add_bridge_output_request

__listOfAddBridgeOutputRequest: TypeAlias = list[
    "capo_mediaconnect.types.add_bridge_output_request.AddBridgeOutputRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAddBridgeOutputRequest) -> list:
    import capo_mediaconnect.types.add_bridge_output_request

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.add_bridge_output_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAddBridgeOutputRequest:
    import capo_mediaconnect.types.add_bridge_output_request

    out: __listOfAddBridgeOutputRequest = []
    for item in data:
        out.append(
            capo_mediaconnect.types.add_bridge_output_request.deserialize_json(item)
        )
    return out
