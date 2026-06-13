"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfSetSourceRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.set_source_request

__listOfSetSourceRequest: TypeAlias = list[
    "aws_sdk_mediaconnect.types.set_source_request.SetSourceRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSetSourceRequest) -> list:
    import aws_sdk_mediaconnect.types.set_source_request

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.set_source_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSetSourceRequest:
    import aws_sdk_mediaconnect.types.set_source_request

    out: __listOfSetSourceRequest = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.set_source_request.deserialize_json(item))
    return out
