"""Generated from Smithy shape ``com.amazonaws.chime#Bot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.bot_type
    import aws_sdk_chime.types.iso8601_timestamp
    import aws_sdk_chime.types.nullable_boolean
    import aws_sdk_chime.types.sensitive_string
    import aws_sdk_chime.types.string


class Bot(TypedDict, closed=True):
    bot_id: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The bot ID.</p>"""
    user_id: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The unique ID for the bot user.</p>"""
    display_name: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The bot display name.</p>"""
    bot_type: NotRequired["aws_sdk_chime.types.bot_type.BotType"]
    """<p>The bot type.</p>"""
    disabled: NotRequired["aws_sdk_chime.types.nullable_boolean.NullableBoolean"]
    """<p>When true, the bot is stopped from running in your account.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The bot creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated bot timestamp, in ISO 8601 format.</p>"""
    bot_email: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The bot email address.</p>"""
    security_token: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The security token used to authenticate Amazon Chime with the outgoing event endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bot) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["BotId"] = value["bot_id"]
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "bot_type" in value:
        import aws_sdk_chime.types.bot_type

        out["BotType"] = aws_sdk_chime.types.bot_type.serialize_json(value["bot_type"])
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "created_timestamp" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["CreatedTimestamp"] = aws_sdk_chime.types.iso8601_timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["UpdatedTimestamp"] = aws_sdk_chime.types.iso8601_timestamp.serialize_json(
            value["updated_timestamp"]
        )
    if "bot_email" in value:
        out["BotEmail"] = value["bot_email"]
    if "security_token" in value:
        out["SecurityToken"] = value["security_token"]
    return out


def deserialize_json(data: dict) -> Bot:
    out: Bot = {}  # type: ignore[typeddict-item]
    if "BotId" in data:
        out["bot_id"] = data["BotId"]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "BotType" in data:
        import aws_sdk_chime.types.bot_type

        out["bot_type"] = aws_sdk_chime.types.bot_type.deserialize_json(data["BotType"])
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    if "CreatedTimestamp" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "BotEmail" in data:
        out["bot_email"] = data["BotEmail"]
    if "SecurityToken" in data:
        out["security_token"] = data["SecurityToken"]
    return out
