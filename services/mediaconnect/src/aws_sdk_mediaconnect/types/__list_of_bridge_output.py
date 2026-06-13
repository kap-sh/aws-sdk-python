"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfBridgeOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.bridge_output

__listOfBridgeOutput: TypeAlias = list[
    "aws_sdk_mediaconnect.types.bridge_output.BridgeOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfBridgeOutput) -> list:
    import aws_sdk_mediaconnect.types.bridge_output

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.bridge_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfBridgeOutput:
    import aws_sdk_mediaconnect.types.bridge_output

    out: __listOfBridgeOutput = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.bridge_output.deserialize_json(item))
    return out
