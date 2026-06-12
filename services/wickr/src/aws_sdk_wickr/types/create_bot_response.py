"""Generated from Smithy shape ``com.amazonaws.wickr#CreateBotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.bot_id
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class CreateBotResponse(TypedDict):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the result of the bot creation operation.</p>"""
    bot_id: "aws_sdk_wickr.types.bot_id.BotId"
    """<p>The unique identifier assigned to the newly created bot.</p>"""
    network_id: NotRequired["aws_sdk_wickr.types.network_id.NetworkId"]
    """<p>The ID of the network where the bot was created.</p>"""
    username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The username of the newly created bot.</p>"""
    display_name: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The display name of the newly created bot.</p>"""
    group_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The ID of the security group to which the bot was assigned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["botId"] = value["bot_id"]
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "username" in value:
        out["username"] = value["username"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> CreateBotResponse:
    out: CreateBotResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    else:
        raise DeserializationError("CreateBotResponse.bot_id required")
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    if "username" in data:
        out["username"] = data["username"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    return out
