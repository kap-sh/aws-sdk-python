"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetChannelPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.policy_text


class GetChannelPolicyResponse(TypedDict, closed=True):
    channel_group_name: "str"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "str"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group.</p>"""
    policy: "capo_mediapackagev2.types.policy_text.PolicyText"
    """<p>The policy assigned to the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelPolicyResponse) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["ChannelName"] = value["channel_name"]
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetChannelPolicyResponse:
    out: GetChannelPolicyResponse = {}  # type: ignore[typeddict-item]
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "GetChannelPolicyResponse.channel_group_name required"
        )
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("GetChannelPolicyResponse.channel_name required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("GetChannelPolicyResponse.policy required")
    return out
