"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfInputSdpLocation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.input_sdp_location

__listOfInputSdpLocation: TypeAlias = list[
    "aws_sdk_medialive.types.input_sdp_location.InputSdpLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputSdpLocation) -> list:
    import aws_sdk_medialive.types.input_sdp_location

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.input_sdp_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputSdpLocation:
    import aws_sdk_medialive.types.input_sdp_location

    out: __listOfInputSdpLocation = []
    for item in data:
        out.append(aws_sdk_medialive.types.input_sdp_location.deserialize_json(item))
    return out
