"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#PutChannelPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.policy_text
    import aws_sdk_mediapackagev2.types.resource_name


class PutChannelPolicyRequest(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    policy: "aws_sdk_mediapackagev2.types.policy_text.PolicyText"
    """<p>The policy to attach to the specified channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutChannelPolicyRequest:
    out: PutChannelPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutChannelPolicyRequest.policy required")
    return out
