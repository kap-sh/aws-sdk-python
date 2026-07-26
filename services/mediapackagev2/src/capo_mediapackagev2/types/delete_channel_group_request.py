"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DeleteChannelGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.resource_name


class DeleteChannelGroupRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteChannelGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteChannelGroupRequest:
    out: DeleteChannelGroupRequest = {}  # type: ignore[typeddict-item]
    return out
