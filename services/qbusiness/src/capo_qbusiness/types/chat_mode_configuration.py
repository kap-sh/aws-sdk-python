"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatModeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.plugin_configuration


class _ChatModeConfiguration_pluginConfiguration(TypedDict, closed=True):
    pluginConfiguration: "capo_qbusiness.types.plugin_configuration.PluginConfiguration"


ChatModeConfiguration: TypeAlias = _ChatModeConfiguration_pluginConfiguration


# --- restJson1 ser/de ---
def serialize_json(value: ChatModeConfiguration) -> dict:
    if "pluginConfiguration" in value:
        import capo_qbusiness.types.plugin_configuration

        return {
            "pluginConfiguration": capo_qbusiness.types.plugin_configuration.serialize_json(
                value["pluginConfiguration"]
            )
        }
    else:
        raise SerializationError("ChatModeConfiguration: no variant present")


def deserialize_json(data: dict) -> ChatModeConfiguration:
    if "pluginConfiguration" in data:
        import capo_qbusiness.types.plugin_configuration

        return {
            "pluginConfiguration": capo_qbusiness.types.plugin_configuration.deserialize_json(
                data["pluginConfiguration"]
            )
        }
    else:
        raise DeserializationError("ChatModeConfiguration: no recognized variant key")
