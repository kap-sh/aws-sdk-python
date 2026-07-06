"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ListChannelMembershipsForAppInstanceUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list
    import aws_sdk_chime_sdk_messaging.types.next_token


class ListChannelMembershipsForAppInstanceUserResponse(TypedDict, closed=True):
    channel_memberships: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list.ChannelMembershipForAppInstanceUserSummaryList"
    ]
    """<p>The information for the requested channel memberships.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested users are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChannelMembershipsForAppInstanceUserResponse) -> dict:
    out: dict = {}
    if "channel_memberships" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list

        out["ChannelMemberships"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list.serialize_json(
                value["channel_memberships"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChannelMembershipsForAppInstanceUserResponse:
    out: ListChannelMembershipsForAppInstanceUserResponse = {}  # type: ignore[typeddict-item]
    if "ChannelMemberships" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list

        out["channel_memberships"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary_list.deserialize_json(
                data["ChannelMemberships"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
