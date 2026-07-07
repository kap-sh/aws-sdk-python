"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelModerator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.identity
    import aws_sdk_chime_sdk_messaging.types.timestamp


class ChannelModerator(TypedDict, closed=True):
    moderator: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The moderator's data.</p>"""
    channel_arn: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The ARN of the moderator's channel.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.timestamp.Timestamp"
    ]
    """<p>The time at which the moderator was created.</p>"""
    created_by: NotRequired["aws_sdk_chime_sdk_messaging.types.identity.Identity"]
    """<p>The <code>AppInstanceUser</code> who created the moderator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelModerator) -> dict:
    out: dict = {}
    if "moderator" in value:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["Moderator"] = aws_sdk_chime_sdk_messaging.types.identity.serialize_json(
            value["moderator"]
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


def deserialize_json(data: dict) -> ChannelModerator:
    out: ChannelModerator = {}  # type: ignore[typeddict-item]
    if "Moderator" in data:
        import aws_sdk_chime_sdk_messaging.types.identity

        out["moderator"] = aws_sdk_chime_sdk_messaging.types.identity.deserialize_json(
            data["Moderator"]
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
