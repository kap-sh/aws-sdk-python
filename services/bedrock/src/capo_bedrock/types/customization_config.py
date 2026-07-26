"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.distillation_config
    import capo_bedrock.types.rft_config


class _CustomizationConfig_distillationConfig(TypedDict, closed=True):
    distillationConfig: "capo_bedrock.types.distillation_config.DistillationConfig"


class _CustomizationConfig_rftConfig(TypedDict, closed=True):
    rftConfig: "capo_bedrock.types.rft_config.RFTConfig"


CustomizationConfig: TypeAlias = (
    _CustomizationConfig_distillationConfig | _CustomizationConfig_rftConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomizationConfig) -> dict:
    if "distillationConfig" in value:
        import capo_bedrock.types.distillation_config

        return {
            "distillationConfig": capo_bedrock.types.distillation_config.serialize_json(
                value["distillationConfig"]
            )
        }
    elif "rftConfig" in value:
        import capo_bedrock.types.rft_config

        return {
            "rftConfig": capo_bedrock.types.rft_config.serialize_json(
                value["rftConfig"]
            )
        }
    else:
        raise SerializationError("CustomizationConfig: no variant present")


def deserialize_json(data: dict) -> CustomizationConfig:
    if "distillationConfig" in data:
        import capo_bedrock.types.distillation_config

        return {
            "distillationConfig": capo_bedrock.types.distillation_config.deserialize_json(
                data["distillationConfig"]
            )
        }
    elif "rftConfig" in data:
        import capo_bedrock.types.rft_config

        return {
            "rftConfig": capo_bedrock.types.rft_config.deserialize_json(
                data["rftConfig"]
            )
        }
    else:
        raise DeserializationError("CustomizationConfig: no recognized variant key")
