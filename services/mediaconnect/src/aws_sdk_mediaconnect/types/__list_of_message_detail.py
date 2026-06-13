"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfMessageDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.message_detail

__listOfMessageDetail: TypeAlias = list[
    "aws_sdk_mediaconnect.types.message_detail.MessageDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMessageDetail) -> list:
    import aws_sdk_mediaconnect.types.message_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.message_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMessageDetail:
    import aws_sdk_mediaconnect.types.message_detail

    out: __listOfMessageDetail = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.message_detail.deserialize_json(item))
    return out
