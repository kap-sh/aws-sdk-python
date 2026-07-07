"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelMembershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.identity
    import aws_sdk_chime_sdk_messaging.types.sub_channel_id


class CreateChannelMembershipResponse(TypedDict, closed=True):
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel.</p>"""
    member: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The ARN and metadata of the member being added.</p>"""
    sub_channel_id: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.sub_channel_id.SubChannelId"
    ]
    """<p>The ID of the SubChannel in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelMembershipResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "member" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["Member"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    if "sub_channel_id" in value:
        out["SubChannelId"] = value["sub_channel_id"]
    return out


def deserialize_json(data: dict) -> CreateChannelMembershipResponse:
    out: CreateChannelMembershipResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "Member" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["member"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    if "SubChannelId" in data:
        out["sub_channel_id"] = data["SubChannelId"]
    return out
