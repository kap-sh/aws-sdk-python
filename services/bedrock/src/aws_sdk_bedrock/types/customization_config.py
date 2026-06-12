"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.rft_config
    import aws_sdk_bedrock.types.distillation_config


class _CustomizationConfig_distillationConfig(TypedDict):
    distillationConfig: "aws_sdk_bedrock.types.distillation_config.DistillationConfig"


class _CustomizationConfig_rftConfig(TypedDict):
    rftConfig: "aws_sdk_bedrock.types.rft_config.RFTConfig"


CustomizationConfig: TypeAlias = (
    _CustomizationConfig_distillationConfig | _CustomizationConfig_rftConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomizationConfig) -> dict:
    if "distillationConfig" in value:
        import aws_sdk_bedrock.types.distillation_config

        return {
            "distillationConfig": aws_sdk_bedrock.types.distillation_config.serialize_json(
                value["distillationConfig"]
            )
        }
    elif "rftConfig" in value:
        import aws_sdk_bedrock.types.rft_config

        return {
            "rftConfig": aws_sdk_bedrock.types.rft_config.serialize_json(
                value["rftConfig"]
            )
        }
    else:
        raise SerializationError("CustomizationConfig: no variant present")


def deserialize_json(data: dict) -> CustomizationConfig:
    if "distillationConfig" in data:
        import aws_sdk_bedrock.types.distillation_config

        return {
            "distillationConfig": aws_sdk_bedrock.types.distillation_config.deserialize_json(
                data["distillationConfig"]
            )
        }
    elif "rftConfig" in data:
        import aws_sdk_bedrock.types.rft_config

        return {
            "rftConfig": aws_sdk_bedrock.types.rft_config.deserialize_json(
                data["rftConfig"]
            )
        }
    else:
        raise DeserializationError("CustomizationConfig: no recognized variant key")
