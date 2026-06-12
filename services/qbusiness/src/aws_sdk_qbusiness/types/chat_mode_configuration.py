"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatModeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.plugin_configuration

class _ChatModeConfiguration_pluginConfiguration(TypedDict):
    pluginConfiguration: "aws_sdk_qbusiness.types.plugin_configuration.PluginConfiguration"

ChatModeConfiguration: TypeAlias = _ChatModeConfiguration_pluginConfiguration

# --- restJson1 ser/de ---
def serialize_json(value: ChatModeConfiguration) -> dict:
    if "pluginConfiguration" in value:
        import aws_sdk_qbusiness.types.plugin_configuration
        return {"pluginConfiguration": aws_sdk_qbusiness.types.plugin_configuration.serialize_json(value["pluginConfiguration"])}
    else:
        raise SerializationError("ChatModeConfiguration: no variant present")


def deserialize_json(data: dict) -> ChatModeConfiguration:
    if "pluginConfiguration" in data:
        import aws_sdk_qbusiness.types.plugin_configuration
        return {"pluginConfiguration": aws_sdk_qbusiness.types.plugin_configuration.deserialize_json(data["pluginConfiguration"])}
    else:
        raise DeserializationError("ChatModeConfiguration: no recognized variant key")