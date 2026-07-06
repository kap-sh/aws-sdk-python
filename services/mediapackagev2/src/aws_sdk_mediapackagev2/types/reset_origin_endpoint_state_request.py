"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResetOriginEndpointStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class ResetOriginEndpointStateRequest(TypedDict, closed=True):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group that contains the channel with the origin endpoint that you are resetting.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel with the origin endpoint that you are resetting.</p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the origin endpoint that you are resetting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetOriginEndpointStateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResetOriginEndpointStateRequest:
    out: ResetOriginEndpointStateRequest = {}  # type: ignore[typeddict-item]
    return out
