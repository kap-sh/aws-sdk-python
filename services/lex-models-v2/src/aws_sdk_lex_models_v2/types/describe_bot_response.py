"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_members
    import aws_sdk_lex_models_v2.types.bot_status
    import aws_sdk_lex_models_v2.types.bot_type
    import aws_sdk_lex_models_v2.types.data_privacy
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.error_log_settings
    import aws_sdk_lex_models_v2.types.failure_reasons
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.role_arn
    import aws_sdk_lex_models_v2.types.session_ttl
    import aws_sdk_lex_models_v2.types.timestamp


class DescribeBotResponse(TypedDict):
    bot_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the bot.</p>"""
    bot_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the bot.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>The description of the bot. </p>"""
    role_arn: NotRequired["aws_sdk_lex_models_v2.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.</p>"""
    data_privacy: NotRequired["aws_sdk_lex_models_v2.types.data_privacy.DataPrivacy"]
    """<p>Settings for managing data privacy of the bot and its conversations with users.</p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "aws_sdk_lex_models_v2.types.session_ttl.SessionTTL"
    ]
    """<p>The maximum time in seconds that Amazon Lex retains the data gathered in a conversation.</p>"""
    bot_status: NotRequired["aws_sdk_lex_models_v2.types.bot_status.BotStatus"]
    """<p>The current status of the bot. When the status is <code>Available</code> the bot is ready to be used in conversations with users.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>A timestamp of the date and time that the bot was last updated.</p>"""
    bot_type: NotRequired["aws_sdk_lex_models_v2.types.bot_type.BotType"]
    """<p>The type of the bot that was described.</p>"""
    bot_members: NotRequired["aws_sdk_lex_models_v2.types.bot_members.BotMembers"]
    """<p>The list of bots in the network that was described.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>If the <code>botStatus</code> is <code>Failed</code>, this contains a list of reasons that the bot couldn't be built.</p>"""
    error_log_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.error_log_settings.ErrorLogSettings"
    ]
    """<p>Contains the configuration for error logging that specifies where and how bot errors are recorded, including destinations like CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "data_privacy" in value:
        import aws_sdk_lex_models_v2.types.data_privacy

        out["dataPrivacy"] = aws_sdk_lex_models_v2.types.data_privacy.serialize_json(
            value["data_privacy"]
        )
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "bot_status" in value:
        import aws_sdk_lex_models_v2.types.bot_status

        out["botStatus"] = aws_sdk_lex_models_v2.types.bot_status.serialize_json(
            value["bot_status"]
        )
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
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
    if "failure_reasons" in value:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failureReasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.serialize_json(
                value["failure_reasons"]
            )
        )
    if "error_log_settings" in value:
        import aws_sdk_lex_models_v2.types.error_log_settings

        out["errorLogSettings"] = (
            aws_sdk_lex_models_v2.types.error_log_settings.serialize_json(
                value["error_log_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeBotResponse:
    out: DescribeBotResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "dataPrivacy" in data:
        import aws_sdk_lex_models_v2.types.data_privacy

        out["data_privacy"] = aws_sdk_lex_models_v2.types.data_privacy.deserialize_json(
            data["dataPrivacy"]
        )
    if "idleSessionTTLInSeconds" in data:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    if "botStatus" in data:
        import aws_sdk_lex_models_v2.types.bot_status

        out["bot_status"] = aws_sdk_lex_models_v2.types.bot_status.deserialize_json(
            data["botStatus"]
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
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
    if "failureReasons" in data:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "errorLogSettings" in data:
        import aws_sdk_lex_models_v2.types.error_log_settings

        out["error_log_settings"] = (
            aws_sdk_lex_models_v2.types.error_log_settings.deserialize_json(
                data["errorLogSettings"]
            )
        )
    return out
