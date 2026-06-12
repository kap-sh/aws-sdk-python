"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_members
    import aws_sdk_lex_models_v2.types.bot_type
    import aws_sdk_lex_models_v2.types.data_privacy
    import aws_sdk_lex_models_v2.types.description
    import aws_sdk_lex_models_v2.types.error_log_settings
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.role_arn
    import aws_sdk_lex_models_v2.types.session_ttl
    import aws_sdk_lex_models_v2.types.tag_map


class CreateBotRequest(TypedDict):
    bot_name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the bot. The bot name must be unique in the account that creates the bot.</p>"""
    description: NotRequired["aws_sdk_lex_models_v2.types.description.Description"]
    """<p>A description of the bot. It appears in lists to help you identify a particular bot.</p>"""
    role_arn: "aws_sdk_lex_models_v2.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.</p>"""
    data_privacy: "aws_sdk_lex_models_v2.types.data_privacy.DataPrivacy"
    """<p>Provides information on additional privacy protections Amazon Lex should use with the bot's data.</p>"""
    idle_session_ttl_in_seconds: "aws_sdk_lex_models_v2.types.session_ttl.SessionTTL"
    """<p>The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.</p>"""
    bot_tags: NotRequired["aws_sdk_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the bot. You can only add tags when you create a bot. You can't use the <code>UpdateBot</code> operation to update tags. To update tags, use the <code>TagResource</code> operation.</p>"""
    test_bot_alias_tags: NotRequired["aws_sdk_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags to add to the test alias for a bot. You can only add tags when you create a bot. You can't use the <code>UpdateAlias</code> operation to update tags. To update tags on the test alias, use the <code>TagResource</code> operation.</p>"""
    bot_type: NotRequired["aws_sdk_lex_models_v2.types.bot_type.BotType"]
    """<p>The type of a bot to create.</p>"""
    bot_members: NotRequired["aws_sdk_lex_models_v2.types.bot_members.BotMembers"]
    """<p>The list of bot members in a network to be created.</p>"""
    error_log_settings: NotRequired[
        "aws_sdk_lex_models_v2.types.error_log_settings.ErrorLogSettings"
    ]
    """<p>Specifies the configuration for error logging during bot creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotRequest) -> dict:
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
    if "bot_tags" in value:
        import aws_sdk_lex_models_v2.types.tag_map

        out["botTags"] = aws_sdk_lex_models_v2.types.tag_map.serialize_json(
            value["bot_tags"]
        )
    if "test_bot_alias_tags" in value:
        import aws_sdk_lex_models_v2.types.tag_map

        out["testBotAliasTags"] = aws_sdk_lex_models_v2.types.tag_map.serialize_json(
            value["test_bot_alias_tags"]
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
    if "error_log_settings" in value:
        import aws_sdk_lex_models_v2.types.error_log_settings

        out["errorLogSettings"] = (
            aws_sdk_lex_models_v2.types.error_log_settings.serialize_json(
                value["error_log_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBotRequest:
    out: CreateBotRequest = {}  # type: ignore[typeddict-item]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    else:
        raise DeserializationError("CreateBotRequest.bot_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateBotRequest.role_arn required")
    if "dataPrivacy" in data:
        import aws_sdk_lex_models_v2.types.data_privacy

        out["data_privacy"] = aws_sdk_lex_models_v2.types.data_privacy.deserialize_json(
            data["dataPrivacy"]
        )
    else:
        raise DeserializationError("CreateBotRequest.data_privacy required")
    if "idleSessionTTLInSeconds" in data:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    else:
        raise DeserializationError(
            "CreateBotRequest.idle_session_ttl_in_seconds required"
        )
    if "botTags" in data:
        import aws_sdk_lex_models_v2.types.tag_map

        out["bot_tags"] = aws_sdk_lex_models_v2.types.tag_map.deserialize_json(
            data["botTags"]
        )
    if "testBotAliasTags" in data:
        import aws_sdk_lex_models_v2.types.tag_map

        out["test_bot_alias_tags"] = (
            aws_sdk_lex_models_v2.types.tag_map.deserialize_json(
                data["testBotAliasTags"]
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
    if "errorLogSettings" in data:
        import aws_sdk_lex_models_v2.types.error_log_settings

        out["error_log_settings"] = (
            aws_sdk_lex_models_v2.types.error_log_settings.deserialize_json(
                data["errorLogSettings"]
            )
        )
    return out
