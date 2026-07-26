"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfBridgeOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.bridge_output

__listOfBridgeOutput: TypeAlias = list[
    "capo_mediaconnect.types.bridge_output.BridgeOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBridgeOutput) -> list:
    import capo_mediaconnect.types.bridge_output

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.bridge_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBridgeOutput:
    import capo_mediaconnect.types.bridge_output

    out: __listOfBridgeOutput = []
    for item in data:
        out.append(capo_mediaconnect.types.bridge_output.deserialize_json(item))
    return out
