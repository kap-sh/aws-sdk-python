"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetOriginEndpointPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class GetOriginEndpointPolicyRequest(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOriginEndpointPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOriginEndpointPolicyRequest:
    out: GetOriginEndpointPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
