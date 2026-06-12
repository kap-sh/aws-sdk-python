"""Generated from Smithy shape ``com.amazonaws.mediapackage#__listOfOriginEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.origin_endpoint

__listOfOriginEndpoint: TypeAlias = list[
    "aws_sdk_mediapackage.types.origin_endpoint.OriginEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOriginEndpoint) -> list:
    import aws_sdk_mediapackage.types.origin_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackage.types.origin_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOriginEndpoint:
    import aws_sdk_mediapackage.types.origin_endpoint

    out: __listOfOriginEndpoint = []
    for item in data:
        out.append(aws_sdk_mediapackage.types.origin_endpoint.deserialize_json(item))
    return out
