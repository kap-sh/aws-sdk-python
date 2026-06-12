"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfProbeResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.probe_result

__listOfProbeResult: TypeAlias = list[
    "aws_sdk_mediaconvert.types.probe_result.ProbeResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfProbeResult) -> list:
    import aws_sdk_mediaconvert.types.probe_result

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.probe_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfProbeResult:
    import aws_sdk_mediaconvert.types.probe_result

    out: __listOfProbeResult = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.probe_result.deserialize_json(item))
    return out
