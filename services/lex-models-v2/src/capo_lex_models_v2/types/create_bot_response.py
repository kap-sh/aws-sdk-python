"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_members
    import capo_lex_models_v2.types.bot_status
    import capo_lex_models_v2.types.bot_type
    import capo_lex_models_v2.types.data_privacy
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.error_log_settings
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.role_arn
    import capo_lex_models_v2.types.session_ttl
    import capo_lex_models_v2.types.tag_map
    import capo_lex_models_v2.types.timestamp


class CreateBotResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>A unique identifier for a particular bot. You use this to identify the bot when you call other Amazon Lex API operations.</p>"""
    bot_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name specified for the bot.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description specified for the bot.</p>"""
    role_arn: NotRequired["capo_lex_models_v2.types.role_arn.RoleArn"]
    """<p>The IAM role specified for the bot.</p>"""
    data_privacy: NotRequired["capo_lex_models_v2.types.data_privacy.DataPrivacy"]
    """<p>The data privacy settings specified for the bot.</p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_lex_models_v2.types.session_ttl.SessionTTL"
    ]
    """<p>The session idle time specified for the bot.</p>"""
    bot_status: NotRequired["capo_lex_models_v2.types.bot_status.BotStatus"]
    """<p>Shows the current status of the bot. The bot is first in the <code>Creating</code> status. Once the bot is read for use, it changes to the <code>Available</code> status. After the bot is created, you can use the <code>DRAFT</code> version of the bot.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp indicating the date and time that the bot was created.</p>"""
    bot_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags associated with the bot.</p>"""
    test_bot_alias_tags: NotRequired["capo_lex_models_v2.types.tag_map.TagMap"]
    """<p>A list of tags associated with the test alias for the bot.</p>"""
    bot_type: NotRequired["capo_lex_models_v2.types.bot_type.BotType"]
    """<p>The type of a bot that was created.</p>"""
    bot_members: NotRequired["capo_lex_models_v2.types.bot_members.BotMembers"]
    """<p>The list of bots in a network that was created.</p>"""
    error_log_settings: NotRequired[
        "capo_lex_models_v2.types.error_log_settings.ErrorLogSettings"
    ]
    """<p>Specifies configuration settings for delivering error logs to Cloudwatch Logs in an Amazon Lex bot response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotResponse) -> dict:
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
        import capo_lex_models_v2.types.data_privacy

        out["dataPrivacy"] = capo_lex_models_v2.types.data_privacy.serialize_json(
            value["data_privacy"]
        )
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "bot_status" in value:
        import capo_lex_models_v2.types.bot_status

        out["botStatus"] = capo_lex_models_v2.types.bot_status.serialize_json(
            value["bot_status"]
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "bot_tags" in value:
        import capo_lex_models_v2.types.tag_map

        out["botTags"] = capo_lex_models_v2.types.tag_map.serialize_json(
            value["bot_tags"]
        )
    if "test_bot_alias_tags" in value:
        import capo_lex_models_v2.types.tag_map

        out["testBotAliasTags"] = capo_lex_models_v2.types.tag_map.serialize_json(
            value["test_bot_alias_tags"]
        )
    if "bot_type" in value:
        import capo_lex_models_v2.types.bot_type

        out["botType"] = capo_lex_models_v2.types.bot_type.serialize_json(
            value["bot_type"]
        )
    if "bot_members" in value:
        import capo_lex_models_v2.types.bot_members

        out["botMembers"] = capo_lex_models_v2.types.bot_members.serialize_json(
            value["bot_members"]
        )
    if "error_log_settings" in value:
        import capo_lex_models_v2.types.error_log_settings

        out["errorLogSettings"] = (
            capo_lex_models_v2.types.error_log_settings.serialize_json(
                value["error_log_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateBotResponse:
    out: CreateBotResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "dataPrivacy" in data:
        import capo_lex_models_v2.types.data_privacy

        out["data_privacy"] = capo_lex_models_v2.types.data_privacy.deserialize_json(
            data["dataPrivacy"]
        )
    if "idleSessionTTLInSeconds" in data:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    if "botStatus" in data:
        import capo_lex_models_v2.types.bot_status

        out["bot_status"] = capo_lex_models_v2.types.bot_status.deserialize_json(
            data["botStatus"]
        )
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "botTags" in data:
        import capo_lex_models_v2.types.tag_map

        out["bot_tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(
            data["botTags"]
        )
    if "testBotAliasTags" in data:
        import capo_lex_models_v2.types.tag_map

        out["test_bot_alias_tags"] = capo_lex_models_v2.types.tag_map.deserialize_json(
            data["testBotAliasTags"]
        )
    if "botType" in data:
        import capo_lex_models_v2.types.bot_type

        out["bot_type"] = capo_lex_models_v2.types.bot_type.deserialize_json(
            data["botType"]
        )
    if "botMembers" in data:
        import capo_lex_models_v2.types.bot_members

        out["bot_members"] = capo_lex_models_v2.types.bot_members.deserialize_json(
            data["botMembers"]
        )
    if "errorLogSettings" in data:
        import capo_lex_models_v2.types.error_log_settings

        out["error_log_settings"] = (
            capo_lex_models_v2.types.error_log_settings.deserialize_json(
                data["errorLogSettings"]
            )
        )
    return out
