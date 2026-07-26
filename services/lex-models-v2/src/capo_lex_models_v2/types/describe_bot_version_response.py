"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_members
    import capo_lex_models_v2.types.bot_status
    import capo_lex_models_v2.types.bot_type
    import capo_lex_models_v2.types.data_privacy
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.numerical_bot_version
    import capo_lex_models_v2.types.parent_bot_networks
    import capo_lex_models_v2.types.role_arn
    import capo_lex_models_v2.types.session_ttl
    import capo_lex_models_v2.types.timestamp


class DescribeBotVersionResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot that contains the version.</p>"""
    bot_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the bot that contains the version.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The version of the bot that was described.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description specified for the bot.</p>"""
    role_arn: NotRequired["capo_lex_models_v2.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot version.</p>"""
    data_privacy: NotRequired["capo_lex_models_v2.types.data_privacy.DataPrivacy"]
    """<p>Data privacy settings for the bot version.</p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "capo_lex_models_v2.types.session_ttl.SessionTTL"
    ]
    """<p>The number of seconds that a session with the bot remains active before it is discarded by Amazon Lex.</p>"""
    bot_status: NotRequired["capo_lex_models_v2.types.bot_status.BotStatus"]
    """<p>The current status of the bot. When the status is <code>Available</code>, the bot version is ready for use.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>If the <code>botStatus</code> is <code>Failed</code>, this contains a list of reasons that the version couldn't be built.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>A timestamp of the date and time that the bot version was created.</p>"""
    parent_bot_networks: NotRequired[
        "capo_lex_models_v2.types.parent_bot_networks.ParentBotNetworks"
    ]
    """<p>A list of the networks to which the bot version you described belongs.</p>"""
    bot_type: NotRequired["capo_lex_models_v2.types.bot_type.BotType"]
    """<p>The type of the bot in the version that was described.</p>"""
    bot_members: NotRequired["capo_lex_models_v2.types.bot_members.BotMembers"]
    """<p>The members of bot network in the version that was described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotVersionResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
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
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "parent_bot_networks" in value:
        import capo_lex_models_v2.types.parent_bot_networks

        out["parentBotNetworks"] = (
            capo_lex_models_v2.types.parent_bot_networks.serialize_json(
                value["parent_bot_networks"]
            )
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
    return out


def deserialize_json(data: dict) -> DescribeBotVersionResponse:
    out: DescribeBotVersionResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
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
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "parentBotNetworks" in data:
        import capo_lex_models_v2.types.parent_bot_networks

        out["parent_bot_networks"] = (
            capo_lex_models_v2.types.parent_bot_networks.deserialize_json(
                data["parentBotNetworks"]
            )
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
    return out
