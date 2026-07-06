"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#BatchCreateChannelMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_type
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.member_arns
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class BatchCreateChannelMembershipRequest(TypedDict, closed=True):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel to which you're adding users or bots.</p>"""
    type: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    ]
    """<p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned. This is only supported by moderators.</p>"""
    member_arns: "aws_sdk_chime_sdk_messaging.types.member_arns.MemberArns"
    """<p>The ARNs of the members you want to add to the channel. Only <code>AppInstanceUsers</code> and <code>AppInstanceBots</code> can be added as a channel member.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request. </p> <note> <p>Only required when creating membership in a SubChannel for a moderator in an elastic channel.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateChannelMembershipRequest) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_type

        out["Type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_type.serialize_json(
                value["type"]
            )
        )
    import aws_sdk_chime_sdk_messaging.types.member_arns

    out["MemberArns"] = aws_sdk_chime_sdk_messaging.types.member_arns.serialize_json(
        value["member_arns"]
    )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> BatchCreateChannelMembershipRequest:
    out: BatchCreateChannelMembershipRequest = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_type

        out["type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_type.deserialize_json(
                data["Type"]
            )
        )
    if "MemberArns" in data:
        import aws_sdk_chime_sdk_messaging.types.member_arns

        out["member_arns"] = (
            aws_sdk_chime_sdk_messaging.types.member_arns.deserialize_json(
                data["MemberArns"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateChannelMembershipRequest.member_arns required"
        )
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
