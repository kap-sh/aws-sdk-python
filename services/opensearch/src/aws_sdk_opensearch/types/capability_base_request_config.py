"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityBaseRequestConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_opensearch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.ai_config


class _CapabilityBaseRequestConfig_aiConfig(TypedDict):
    aiConfig: "aws_sdk_opensearch.types.ai_config.AIConfig"


CapabilityBaseRequestConfig: TypeAlias = _CapabilityBaseRequestConfig_aiConfig


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityBaseRequestConfig) -> dict:
    if "aiConfig" in value:
        import aws_sdk_opensearch.types.ai_config

        return {
            "aiConfig": aws_sdk_opensearch.types.ai_config.serialize_json(
                value["aiConfig"]
            )
        }
    else:
        raise SerializationError("CapabilityBaseRequestConfig: no variant present")


def deserialize_json(data: dict) -> CapabilityBaseRequestConfig:
    if "aiConfig" in data:
        import aws_sdk_opensearch.types.ai_config

        return {
            "aiConfig": aws_sdk_opensearch.types.ai_config.deserialize_json(
                data["aiConfig"]
            )
        }
    else:
        raise DeserializationError(
            "CapabilityBaseRequestConfig: no recognized variant key"
        )
