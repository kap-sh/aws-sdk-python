"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ResetChannelStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class ResetChannelStateRequest(TypedDict, closed=True):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group that contains the channel that you are resetting.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel that you are resetting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetChannelStateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResetChannelStateRequest:
    out: ResetChannelStateRequest = {}  # type: ignore[typeddict-item]
    return out
