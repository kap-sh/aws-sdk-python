"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelBan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.identity
    import aws_sdk_chime_sdk_messaging.types.timestamp


class ChannelBan(TypedDict, closed=True):
    member: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The member being banned from the channel.</p>"""
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the channel from which a member is being banned.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which the ban was created.</p>"""
    created_by: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The <code>AppInstanceUser</code> who created the ban.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelBan) -> dict:
    out: dict = {}
    if "member" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["Member"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["member"]
        )
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "created_by" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["CreatedBy"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["created_by"]
        )
    return out


def deserialize_json(data: dict) -> ChannelBan:
    out: ChannelBan = {}  # type: ignore[typeddict-item]
    if "Member" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["member"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["Member"]
        )
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_messaging.types.timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_messaging.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "CreatedBy" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["created_by"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["CreatedBy"]
        )
    return out
