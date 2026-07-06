"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DeleteChannelPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class DeleteChannelPolicyRequest(TypedDict, closed=True):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelPolicyRequest:
    out: DeleteChannelPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
