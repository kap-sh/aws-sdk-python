"""Generated from Smithy shape ``com.amazonaws.wickr#GetDataRetentionBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string


class GetDataRetentionBotResponse(TypedDict, closed=True):
    bot_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The name of the data retention bot.</p>"""
    bot_exists: NotRequired["bool"]
    """<p>Indicates whether a data retention bot exists in the network.</p>"""
    is_bot_active: NotRequired["bool"]
    """<p>Indicates whether the data retention bot is active and operational.</p>"""
    is_data_retention_bot_registered: NotRequired["bool"]
    """<p>Indicates whether the data retention bot has been registered with the network.</p>"""
    is_data_retention_service_enabled: NotRequired["bool"]
    """<p>Indicates whether the data retention service is enabled for the network.</p>"""
    is_pubkey_msg_acked: NotRequired["bool"]
    """<p>Indicates whether the public key message has been acknowledged by the bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataRetentionBotResponse) -> dict:
    out: dict = {}
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    if "bot_exists" in value:
        out["botExists"] = value["bot_exists"]
    if "is_bot_active" in value:
        out["isBotActive"] = value["is_bot_active"]
    if "is_data_retention_bot_registered" in value:
        out["isDataRetentionBotRegistered"] = value["is_data_retention_bot_registered"]
    if "is_data_retention_service_enabled" in value:
        out["isDataRetentionServiceEnabled"] = value[
            "is_data_retention_service_enabled"
        ]
    if "is_pubkey_msg_acked" in value:
        out["isPubkeyMsgAcked"] = value["is_pubkey_msg_acked"]
    return out


def deserialize_json(data: dict) -> GetDataRetentionBotResponse:
    out: GetDataRetentionBotResponse = {}  # type: ignore[typeddict-item]
    if "botName" in data:
        out["bot_name"] = data["botName"]
    if "botExists" in data:
        out["bot_exists"] = data["botExists"]
    if "isBotActive" in data:
        out["is_bot_active"] = data["isBotActive"]
    if "isDataRetentionBotRegistered" in data:
        out["is_data_retention_bot_registered"] = data["isDataRetentionBotRegistered"]
    if "isDataRetentionServiceEnabled" in data:
        out["is_data_retention_service_enabled"] = data["isDataRetentionServiceEnabled"]
    if "isPubkeyMsgAcked" in data:
        out["is_pubkey_msg_acked"] = data["isPubkeyMsgAcked"]
    return out
