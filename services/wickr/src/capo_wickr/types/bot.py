"""Generated from Smithy shape ``com.amazonaws.wickr#Bot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.bot_status
    import capo_wickr.types.generic_string


class Bot(TypedDict, closed=True):
    bot_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The unique identifier of the bot.</p>"""
    display_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The display name of the bot that is visible to users.</p>"""
    username: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The username of the bot.</p>"""
    uname: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The unique username hash identifier for the bot.</p>"""
    pubkey: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The public key of the bot used for encryption.</p>"""
    status: NotRequired["capo_wickr.types.bot_status.BotStatus"]
    """<p>The current status of the bot (1 for pending, 2 for active).</p>"""
    group_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The ID of the security group to which the bot belongs.</p>"""
    has_challenge: NotRequired["bool"]
    """<p>Indicates whether the bot has a password set.</p>"""
    suspended: NotRequired["bool"]
    """<p>Indicates whether the bot is currently suspended.</p>"""
    last_login: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The timestamp of the bot's last login.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bot) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "username" in value:
        out["username"] = value["username"]
    if "uname" in value:
        out["uname"] = value["uname"]
    if "pubkey" in value:
        out["pubkey"] = value["pubkey"]
    if "status" in value:
        import capo_wickr.types.bot_status

        out["status"] = capo_wickr.types.bot_status.serialize_json(value["status"])
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "has_challenge" in value:
        out["hasChallenge"] = value["has_challenge"]
    if "suspended" in value:
        out["suspended"] = value["suspended"]
    if "last_login" in value:
        out["lastLogin"] = value["last_login"]
    return out


def deserialize_json(data: dict) -> Bot:
    out: Bot = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "username" in data:
        out["username"] = data["username"]
    if "uname" in data:
        out["uname"] = data["uname"]
    if "pubkey" in data:
        out["pubkey"] = data["pubkey"]
    if "status" in data:
        import capo_wickr.types.bot_status

        out["status"] = capo_wickr.types.bot_status.deserialize_json(data["status"])
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "hasChallenge" in data:
        out["has_challenge"] = data["hasChallenge"]
    if "suspended" in data:
        out["suspended"] = data["suspended"]
    if "lastLogin" in data:
        out["last_login"] = data["lastLogin"]
    return out
