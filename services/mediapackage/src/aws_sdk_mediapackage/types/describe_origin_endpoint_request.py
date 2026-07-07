"""Generated from Smithy shape ``com.amazonaws.mediapackage#DescribeOriginEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class DescribeOriginEndpointRequest(TypedDict, closed=True):
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the OriginEndpoint."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOriginEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeOriginEndpointRequest:
    out: DescribeOriginEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
