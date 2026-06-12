"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelMembershipRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_type
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class CreateChannelMembershipRequest(TypedDict):
    channel_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel to which you're adding users.</p>"""
    member_arn: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The <code>AppInstanceUserArn</code> of the member you want to add to the channel.</p>"""
    type: "aws_sdk_chime_sdk_messaging.types.channel_membership_type.ChannelMembershipType"
    """<p>The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned. This is only supported by moderators.</p>"""
    chime_bearer: "aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the request.</p> <note> <p>Only required when creating membership in a SubChannel for a moderator in an elastic channel.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelMembershipRequest) -> dict:
    out: dict = {}
    out["MemberArn"] = value["member_arn"]
    import aws_sdk_chime_sdk_messaging.types.channel_membership_type

    out["Type"] = (
        aws_sdk_chime_sdk_messaging.types.channel_membership_type.serialize_json(
            value["type"]
        )
    )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> CreateChannelMembershipRequest:
    out: CreateChannelMembershipRequest = {}  # type: ignore[typeddict-item]
    if "MemberArn" in data:
        out["member_arn"] = data["MemberArn"]
    else:
        raise DeserializationError("CreateChannelMembershipRequest.member_arn required")
    if "Type" in data:
        import aws_sdk_chime_sdk_messaging.types.channel_membership_type

        out["type"] = (
            aws_sdk_chime_sdk_messaging.types.channel_membership_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CreateChannelMembershipRequest.type required")
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
