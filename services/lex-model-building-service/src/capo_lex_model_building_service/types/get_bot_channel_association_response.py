"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#GetBotChannelAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.alias_name
    import capo_lex_model_building_service.types.bot_channel_name
    import capo_lex_model_building_service.types.bot_name
    import capo_lex_model_building_service.types.channel_configuration_map
    import capo_lex_model_building_service.types.channel_status
    import capo_lex_model_building_service.types.channel_type
    import capo_lex_model_building_service.types.description
    import capo_lex_model_building_service.types.string
    import capo_lex_model_building_service.types.timestamp


class GetBotChannelAssociationResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_lex_model_building_service.types.bot_channel_name.BotChannelName"
    ]
    """<p>The name of the association between the bot and the channel.</p>"""
    description: NotRequired[
        "capo_lex_model_building_service.types.description.Description"
    ]
    """<p>A description of the association between the bot and the channel.</p>"""
    bot_alias: NotRequired["capo_lex_model_building_service.types.alias_name.AliasName"]
    """<p>An alias pointing to the specific version of the Amazon Lex bot to which this association is being made.</p>"""
    bot_name: NotRequired["capo_lex_model_building_service.types.bot_name.BotName"]
    """<p>The name of the Amazon Lex bot.</p>"""
    created_date: NotRequired[
        "capo_lex_model_building_service.types.timestamp.Timestamp"
    ]
    """<p>The date that the association between the bot and the channel was created.</p>"""
    type: NotRequired["capo_lex_model_building_service.types.channel_type.ChannelType"]
    """<p>The type of the messaging platform.</p>"""
    bot_configuration: NotRequired[
        "capo_lex_model_building_service.types.channel_configuration_map.ChannelConfigurationMap"
    ]
    """<p>Provides information that the messaging platform needs to communicate with the Amazon Lex bot.</p>"""
    status: NotRequired[
        "capo_lex_model_building_service.types.channel_status.ChannelStatus"
    ]
    """<p>The status of the bot channel. </p> <ul> <li> <p> <code>CREATED</code> - The channel has been created and is ready for use.</p> </li> <li> <p> <code>IN_PROGRESS</code> - Channel creation is in progress.</p> </li> <li> <p> <code>FAILED</code> - There was an error creating the channel. For information about the reason for the failure, see the <code>failureReason</code> field.</p> </li> </ul>"""
    failure_reason: NotRequired["capo_lex_model_building_service.types.string.String"]
    """<p>If <code>status</code> is <code>FAILED</code>, Amazon Lex provides the reason that it failed to create the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBotChannelAssociationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "bot_alias" in value:
        out["botAlias"] = value["bot_alias"]
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "created_date" in value:
        import capo_lex_model_building_service.types.timestamp

        out["createdDate"] = (
            capo_lex_model_building_service.types.timestamp.serialize_json(
                value["created_date"]
            )
        )
    if "type" in value:
        import capo_lex_model_building_service.types.channel_type

        out["type"] = capo_lex_model_building_service.types.channel_type.serialize_json(
            value["type"]
        )
    if "bot_configuration" in value:
        import capo_lex_model_building_service.types.channel_configuration_map

        out["botConfiguration"] = (
            capo_lex_model_building_service.types.channel_configuration_map.serialize_json(
                value["bot_configuration"]
            )
        )
    if "status" in value:
        import capo_lex_model_building_service.types.channel_status

        out["status"] = (
            capo_lex_model_building_service.types.channel_status.serialize_json(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> GetBotChannelAssociationResponse:
    out: GetBotChannelAssociationResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "botAlias" in data:
        out["bot_alias"] = data["botAlias"]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "createdDate" in data:
        import capo_lex_model_building_service.types.timestamp

        out["created_date"] = (
            capo_lex_model_building_service.types.timestamp.deserialize_json(
                data["createdDate"]
            )
        )
    if "type" in data:
        import capo_lex_model_building_service.types.channel_type

        out["type"] = (
            capo_lex_model_building_service.types.channel_type.deserialize_json(
                data["type"]
            )
        )
    if "botConfiguration" in data:
        import capo_lex_model_building_service.types.channel_configuration_map

        out["bot_configuration"] = (
            capo_lex_model_building_service.types.channel_configuration_map.deserialize_json(
                data["botConfiguration"]
            )
        )
    if "status" in data:
        import capo_lex_model_building_service.types.channel_status

        out["status"] = (
            capo_lex_model_building_service.types.channel_status.deserialize_json(
                data["status"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
