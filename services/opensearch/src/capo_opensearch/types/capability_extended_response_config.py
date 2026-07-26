"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityExtendedResponseConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_opensearch.types.ai_config


class _CapabilityExtendedResponseConfig_aiConfig(TypedDict, closed=True):
    aiConfig: "capo_opensearch.types.ai_config.AIConfig"


CapabilityExtendedResponseConfig: TypeAlias = _CapabilityExtendedResponseConfig_aiConfig


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityExtendedResponseConfig) -> dict:
    if "aiConfig" in value:
        import capo_opensearch.types.ai_config

        return {
            "aiConfig": capo_opensearch.types.ai_config.serialize_json(
                value["aiConfig"]
            )
        }
    else:
        raise SerializationError("CapabilityExtendedResponseConfig: no variant present")


def deserialize_json(data: dict) -> CapabilityExtendedResponseConfig:
    if "aiConfig" in data:
        import capo_opensearch.types.ai_config

        return {
            "aiConfig": capo_opensearch.types.ai_config.deserialize_json(
                data["aiConfig"]
            )
        }
    else:
        raise DeserializationError(
            "CapabilityExtendedResponseConfig: no recognized variant key"
        )
