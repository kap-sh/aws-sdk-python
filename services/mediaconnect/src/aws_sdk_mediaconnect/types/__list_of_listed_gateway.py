"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfListedGateway``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.listed_gateway

__listOfListedGateway: TypeAlias = list[
    "aws_sdk_mediaconnect.types.listed_gateway.ListedGateway"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfListedGateway) -> list:
    import aws_sdk_mediaconnect.types.listed_gateway

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconnect.types.listed_gateway.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfListedGateway:
    import aws_sdk_mediaconnect.types.listed_gateway

    out: __listOfListedGateway = []
    for item in data:
        out.append(aws_sdk_mediaconnect.types.listed_gateway.deserialize_json(item))
    return out
