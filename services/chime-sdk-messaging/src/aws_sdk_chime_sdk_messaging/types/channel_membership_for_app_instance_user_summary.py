"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipForAppInstanceUserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.app_instance_user_membership_summary
    import aws_sdk_chime_sdk_messaging.types.channel_summary


class ChannelMembershipForAppInstanceUserSummary(TypedDict, closed=True):
    channel_summary: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_summary.ChannelSummary"
    ]
    """<p>Returns the channel data for an <code>AppInstance</code>.</p>"""
    app_instance_user_membership_summary: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.app_instance_user_membership_summary.AppInstanceUserMembershipSummary"
    ]
    """<p>Returns the channel membership data for an <code>AppInstance</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipForAppInstanceUserSummary) -> dict:
    out: dict = {}
    if "channel_summary" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_summary

        out["ChannelSummary"] = (
            aws_sdk_chime_sdk_messaging.types.channel_summary.serialize_json(
                value["channel_summary"]
            )
        )
    if "app_instance_user_membership_summary" in value:
        import aws_sdk_chime_sdk_messaging.types.app_instance_user_membership_summary

        out["AppInstanceUserMembershipSummary"] = (
            aws_sdk_chime_sdk_messaging.types.app_instance_user_membership_summary.serialize_json(
                value["app_instance_user_membership_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChannelMembershipForAppInstanceUserSummary:
    out: ChannelMembershipForAppInstanceUserSummary = {}  # type: ignore[typeddict-item]
    if "ChannelSummary" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_summary

        out["channel_summary"] = (
            aws_sdk_chime_sdk_messaging.types.channel_summary.deserialize_json(
                data["ChannelSummary"]
            )
        )
    if "AppInstanceUserMembershipSummary" in data:
        import aws_sdk_chime_sdk_messaging.types.app_instance_user_membership_summary

        out["app_instance_user_membership_summary"] = (
            aws_sdk_chime_sdk_messaging.types.app_instance_user_membership_summary.deserialize_json(
                data["AppInstanceUserMembershipSummary"]
            )
        )
    return out
