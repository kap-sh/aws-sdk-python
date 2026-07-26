"""Generated from Smithy shape ``com.amazonaws.chime#RetentionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.conversation_retention_settings
    import capo_chime.types.room_retention_settings


class RetentionSettings(TypedDict, closed=True):
    room_retention_settings: NotRequired[
        "capo_chime.types.room_retention_settings.RoomRetentionSettings"
    ]
    """<p>The chat room retention settings.</p>"""
    conversation_retention_settings: NotRequired[
        "capo_chime.types.conversation_retention_settings.ConversationRetentionSettings"
    ]
    """<p>The chat conversation retention settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetentionSettings) -> dict:
    out: dict = {}
    if "room_retention_settings" in value:
        import capo_chime.types.room_retention_settings

        out["RoomRetentionSettings"] = (
            capo_chime.types.room_retention_settings.serialize_json(
                value["room_retention_settings"]
            )
        )
    if "conversation_retention_settings" in value:
        import capo_chime.types.conversation_retention_settings

        out["ConversationRetentionSettings"] = (
            capo_chime.types.conversation_retention_settings.serialize_json(
                value["conversation_retention_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetentionSettings:
    out: RetentionSettings = {}  # type: ignore[typeddict-item]
    if "RoomRetentionSettings" in data:
        import capo_chime.types.room_retention_settings

        out["room_retention_settings"] = (
            capo_chime.types.room_retention_settings.deserialize_json(
                data["RoomRetentionSettings"]
            )
        )
    if "ConversationRetentionSettings" in data:
        import capo_chime.types.conversation_retention_settings

        out["conversation_retention_settings"] = (
            capo_chime.types.conversation_retention_settings.deserialize_json(
                data["ConversationRetentionSettings"]
            )
        )
    return out
