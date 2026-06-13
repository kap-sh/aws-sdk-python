"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfAddBridgeOutputRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.add_bridge_output_request

__listOfAddBridgeOutputRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.add_bridge_output_request.AddBridgeOutputRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAddBridgeOutputRequest) -> list:
    import aws_sdk_mediaconnect.types.add_bridge_output_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.add_bridge_output_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfAddBridgeOutputRequest:
    import aws_sdk_mediaconnect.types.add_bridge_output_request

    out: __listOfAddBridgeOutputRequest = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.add_bridge_output_request.deserialize_json(item)
        )
    return out
