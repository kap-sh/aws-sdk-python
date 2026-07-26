"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMembershipsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_summary_list
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.next_token


class ListChannelMembershipsResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    channel_memberships: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_summary_list.ChannelMembershipSummaryList"
    ]
    """<p>The information for the requested channel memberships.</p>"""
    next_token: NotRequired["capo_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested channel memberships are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMembershipsResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "channel_memberships" in value:
        import capo_chime_sdk_messaging.types.channel_membership_summary_list

        out["ChannelMemberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_summary_list.serialize_json(
                value["channel_memberships"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelMembershipsResponse:
    out: ListChannelMembershipsResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "ChannelMemberships" in data:
        import capo_chime_sdk_messaging.types.channel_membership_summary_list

        out["channel_memberships"] = (
            capo_chime_sdk_messaging.types.channel_membership_summary_list.deserialize_json(
                data["ChannelMemberships"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
