"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfListedFlow``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_flow

__listOfListedFlow: TypeAlias = list[
    "aws_sdk_mediaconnect.types.listed_flow.ListedFlow"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListedFlow) -> list:
    import aws_sdk_mediaconnect.types.listed_flow

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.listed_flow.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfListedFlow:
    import aws_sdk_mediaconnect.types.listed_flow

    out: __listOfListedFlow = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.listed_flow.deserialize_json(item))
    return out
