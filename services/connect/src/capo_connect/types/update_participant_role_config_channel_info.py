"""Generated from Smithy shape ``com.amazonaws.connect#UpdateParticipantRoleConfigChannelInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.chat_participant_role_config


class _UpdateParticipantRoleConfigChannelInfo_Chat(TypedDict, closed=True):
    Chat: "capo_connect.types.chat_participant_role_config.ChatParticipantRoleConfig"


UpdateParticipantRoleConfigChannelInfo: TypeAlias = (
    _UpdateParticipantRoleConfigChannelInfo_Chat
)


# --- restJson1 ser/de ---
def serialize_json(value: UpdateParticipantRoleConfigChannelInfo) -> dict:
    if "Chat" in value:
        import capo_connect.types.chat_participant_role_config

        return {
            "Chat": capo_connect.types.chat_participant_role_config.serialize_json(
                value["Chat"]
            )
        }
    else:
        raise SerializationError(
            "UpdateParticipantRoleConfigChannelInfo: no variant present"
        )


def deserialize_json(data: dict) -> UpdateParticipantRoleConfigChannelInfo:
    if "Chat" in data:
        import capo_connect.types.chat_participant_role_config

        return {
            "Chat": capo_connect.types.chat_participant_role_config.deserialize_json(
                data["Chat"]
            )
        }
    else:
        raise DeserializationError(
            "UpdateParticipantRoleConfigChannelInfo: no recognized variant key"
        )
