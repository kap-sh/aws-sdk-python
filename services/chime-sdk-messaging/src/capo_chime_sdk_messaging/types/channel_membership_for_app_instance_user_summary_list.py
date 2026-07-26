"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipForAppInstanceUserSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

ChannelMembershipForAppInstanceUserSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.ChannelMembershipForAppInstanceUserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipForAppInstanceUserSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelMembershipForAppInstanceUserSummaryList:
    import capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary

    out: ChannelMembershipForAppInstanceUserSummaryList = []
    for item in data:
        out.append(
            capo_chime_sdk_messaging.types.channel_membership_for_app_instance_user_summary.deserialize_json(
                item
            )
        )
    return out
