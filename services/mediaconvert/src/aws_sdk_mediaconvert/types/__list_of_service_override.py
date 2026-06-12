"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfServiceOverride``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.service_override

__listOfServiceOverride: TypeAlias = list[
    "aws_sdk_mediaconvert.types.service_override.ServiceOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfServiceOverride) -> list:
    import aws_sdk_mediaconvert.types.service_override

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.service_override.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfServiceOverride:
    import aws_sdk_mediaconvert.types.service_override

    out: __listOfServiceOverride = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.service_override.deserialize_json(item))
    return out
