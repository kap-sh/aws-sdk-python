"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_members
    import aws_sdk_lex_models_v2.types.bot_type
    import aws_sdk_lex_models_v2.types.data_privacy
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.error_log_settings
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.role_arn
    import aws_sdk_lex_models_v2.types.session_ttl


class UpdateBotRequest(TypedDict):
    bot_id: "aws_sdk_lex_models_v2.types.id.Id"
    """<p>The unique identifier of the bot to update. This identifier is returned by the <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html\">CreateBot</a> operation.</p>"""
    bot_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The new name of the bot. The name must be unique in the account that creates the bot.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>A description of the bot.</p>"""
    role_arn: "aws_sdk_lex_models_v2.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the bot.</p>"""
    data_privacy: "aws_sdk_lex_models_v2.types.data_privacy.DataPrivacy"
    """<p>Provides information on additional privacy protections Amazon Lex should use with the bot's data.</p>"""
    idle_session_ttl_in_seconds: "aws_sdk_lex_models_v2.types.session_ttl.SessionTTL"
    """<p>The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.</p>"""
    bot_type: NotRequired["aws_sdk_lex_models_v2.types.bot_type.BotType"]
    """<p>The type of the bot to be updated.</p>"""
    bot_members: NotRequired["aws_sdk_lex_models_v2.types.bot_members.BotMembers"]
    """<p>The list of bot members in the network associated with the update action.</p>"""
    error_log_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.error_log_settings.ErrorLogSettings"
    ]
    """<p>Allows you to modify how Amazon Lex logs errors during bot interactions, including destinations for error logs and the types of errors to be captured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotRequest) -> dict:
    out: dict = {}
    out["botName"] = value["bot_name"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    import aws_sdk_lex_models_v2.types.data_privacy

    out["dataPrivacy"] = aws_sdk_lex_models_v2.types.data_privacy.serialize_json(
        value["data_privacy"]
    )
    out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "bot_type" in value:
        import aws_sdk_lex_models_v2.types.bot_type

        out["botType"] = aws_sdk_lex_models_v2.types.bot_type.serialize_json(
            value["bot_type"]
        )
    if "bot_members" in value:
        import aws_sdk_lex_models_v2.types.bot_members

        out["botMembers"] = aws_sdk_lex_models_v2.types.bot_members.serialize_json(
            value["bot_members"]
        )
    if "error_log_settings" in value:
        import aws_sdk_lex_models_v2.types.error_log_settings

        out["errorLogSettings"] = (
            aws_sdk_lex_models_v2.types.error_log_settings.serialize_json(
                value["error_log_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBotRequest:
    out: UpdateBotRequest = {}  # type: ignore[typeddict-item]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    else:
        raise DeserializationError("UpdateBotRequest.bot_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdateBotRequest.role_arn required")
    if "dataPrivacy" in data:
        import aws_sdk_lex_models_v2.types.data_privacy

        out["data_privacy"] = aws_sdk_lex_models_v2.types.data_privacy.deserialize_json(
            data["dataPrivacy"]
        )
    else:
        raise DeserializationError("UpdateBotRequest.data_privacy required")
    if "idleSessionTTLInSeconds" in data:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    else:
        raise DeserializationError(
            "UpdateBotRequest.idle_session_ttl_in_seconds required"
        )
    if "botType" in data:
        import aws_sdk_lex_models_v2.types.bot_type

        out["bot_type"] = aws_sdk_lex_models_v2.types.bot_type.deserialize_json(
            data["botType"]
        )
    if "botMembers" in data:
        import aws_sdk_lex_models_v2.types.bot_members

        out["bot_members"] = aws_sdk_lex_models_v2.types.bot_members.deserialize_json(
            data["botMembers"]
        )
    if "errorLogSettings" in data:
        import aws_sdk_lex_models_v2.types.error_log_settings

        out["error_log_settings"] = (
            aws_sdk_lex_models_v2.types.error_log_settings.deserialize_json(
                data["errorLogSettings"]
            )
        )
    return out
