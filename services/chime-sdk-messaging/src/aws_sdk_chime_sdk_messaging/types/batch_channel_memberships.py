"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchChannelMemberships``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_type
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.identity
    import aws_sdk_chime_sdk_messaging.types.members
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class BatchChannelMemberships(TypedDict, closed=True):
    invited_by: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The identifier of the member who invited another member.</p>"""
    type: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    ]
    """<p>The membership types set for the channel members.</p>"""
    members: NotRequired["aws_sdk_chime_sdk_messaging.types.members.Members"]
    """<p>The users successfully added to the request.</p>"""
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel to which you're adding members.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchChannelMemberships) -> dict:
    out: dict = {}
    if "invited_by" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["InvitedBy"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["invited_by"]
        )
    if "type" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_type

        out["Type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_type.serialize_json(
                value["type"]
            )
        )
    if "members" in value:
        import aws_sdk_chime_sdk_messaging.types.members

        out["Members"] = aws_sdk_chime_sdk_messaging.types.members.serialize_json(
            value["members"]
        )
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> BatchChannelMemberships:
    out: BatchChannelMemberships = {}  # type: ignore[typeddict-item]
    if "InvitedBy" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["invited_by"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["InvitedBy"]
        )
    if "Type" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_type

        out["type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_type.deserialize_json(
                data["Type"]
            )
        )
    if "Members" in data:
        import aws_sdk_chime_sdk_messaging.types.members

        out["members"] = aws_sdk_chime_sdk_messaging.types.members.deserialize_json(
            data["Members"]
        )
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
