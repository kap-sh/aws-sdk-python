"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_membership_type
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.identity
    import capo_chime_sdk_messaging.types.sub_channel_id
    import capo_chime_sdk_messaging.types.timestamp


class ChannelMembership(TypedDict, closed=True):
    invited_by: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The identifier of the member who invited another member.</p>"""
    type: NotRequired[
        "capo_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    ]
    """<p>The membership type set for the channel member.</p>"""
    member: NotRequired["capo_chime_sdk_messaging.types.identity.Identity"]
    """<p>The data of the channel member.</p>"""
    channel_arn: NotRequired["capo_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the member's channel.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_messaging.types.timestamp.Timestamp"]
    """<p>The time at which the channel membership was created.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which a channel membership was last updated.</p>"""
    sub_channel_id: NotRequired[
        "capo_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel that a user belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembership) -> dict:
    out: dict = {}
    if "invited_by" in value:
        import capo_chime_sdk_messaging.types.identity

        out["InvitedBy"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["invited_by"]
        )
    if "type" in value:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["Type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.serialize_json(
                value["type"]
            )
        )
    if "member" in value:
        import capo_chime_sdk_messaging.types.identity

        out["Member"] = capo_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "created_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_messaging.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> ChannelMembership:
    out: ChannelMembership = {}  # type: ignore[typeddict-item]
    if "InvitedBy" in data:
        import capo_chime_sdk_messaging.types.identity

        out["invited_by"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["InvitedBy"]
        )
    if "Type" in data:
        import capo_chime_sdk_messaging.types.channel_membership_type

        out["type"] = (
            capo_chime_sdk_messaging.types.channel_membership_type.deserialize_json(
                data["Type"]
            )
        )
    if "Member" in data:
        import capo_chime_sdk_messaging.types.identity

        out["member"] = capo_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "CreatedTimestamp" in data:
        import capo_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "LastUpdatedTimestamp" in data:
        import capo_chime_sdk_messaging.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
