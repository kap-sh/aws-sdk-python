"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_compilation_config
    import aws_sdk_sagemaker.types.model_quantization_config
    import aws_sdk_sagemaker.types.model_sharding_config
    import aws_sdk_sagemaker.types.model_speculative_decoding_config


class _OptimizationConfig_ModelQuantizationConfig(TypedDict):
    ModelQuantizationConfig: (
        "aws_sdk_sagemaker.types.model_quantization_config.ModelQuantizationConfig"
    )


class _OptimizationConfig_ModelCompilationConfig(TypedDict):
    ModelCompilationConfig: (
        "aws_sdk_sagemaker.types.model_compilation_config.ModelCompilationConfig"
    )


class _OptimizationConfig_ModelShardingConfig(TypedDict):
    ModelShardingConfig: (
        "aws_sdk_sagemaker.types.model_sharding_config.ModelShardingConfig"
    )


class _OptimizationConfig_ModelSpeculativeDecodingConfig(TypedDict):
    ModelSpeculativeDecodingConfig: "aws_sdk_sagemaker.types.model_speculative_decoding_config.ModelSpeculativeDecodingConfig"


OptimizationConfig: TypeAlias = (
    _OptimizationConfig_ModelQuantizationConfig
    | _OptimizationConfig_ModelCompilationConfig
    | _OptimizationConfig_ModelShardingConfig
    | _OptimizationConfig_ModelSpeculativeDecodingConfig
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationConfig) -> dict:
    if "ModelQuantizationConfig" in value:
        import aws_sdk_sagemaker.types.model_quantization_config

        return {
            "ModelQuantizationConfig": aws_sdk_sagemaker.types.model_quantization_config.serialize_aws_json_1_1(
                value["ModelQuantizationConfig"]
            )
        }
    elif "ModelCompilationConfig" in value:
        import aws_sdk_sagemaker.types.model_compilation_config

        return {
            "ModelCompilationConfig": aws_sdk_sagemaker.types.model_compilation_config.serialize_aws_json_1_1(
                value["ModelCompilationConfig"]
            )
        }
    elif "ModelShardingConfig" in value:
        import aws_sdk_sagemaker.types.model_sharding_config

        return {
            "ModelShardingConfig": aws_sdk_sagemaker.types.model_sharding_config.serialize_aws_json_1_1(
                value["ModelShardingConfig"]
            )
        }
    elif "ModelSpeculativeDecodingConfig" in value:
        import aws_sdk_sagemaker.types.model_speculative_decoding_config

        return {
            "ModelSpeculativeDecodingConfig": aws_sdk_sagemaker.types.model_speculative_decoding_config.serialize_aws_json_1_1(
                value["ModelSpeculativeDecodingConfig"]
            )
        }
    else:
        raise SerializationError("OptimizationConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> OptimizationConfig:
    if "ModelQuantizationConfig" in data:
        import aws_sdk_sagemaker.types.model_quantization_config

        return {
            "ModelQuantizationConfig": aws_sdk_sagemaker.types.model_quantization_config.deserialize_aws_json_1_1(
                data["ModelQuantizationConfig"]
            )
        }
    elif "ModelCompilationConfig" in data:
        import aws_sdk_sagemaker.types.model_compilation_config

        return {
            "ModelCompilationConfig": aws_sdk_sagemaker.types.model_compilation_config.deserialize_aws_json_1_1(
                data["ModelCompilationConfig"]
            )
        }
    elif "ModelShardingConfig" in data:
        import aws_sdk_sagemaker.types.model_sharding_config

        return {
            "ModelShardingConfig": aws_sdk_sagemaker.types.model_sharding_config.deserialize_aws_json_1_1(
                data["ModelShardingConfig"]
            )
        }
    elif "ModelSpeculativeDecodingConfig" in data:
        import aws_sdk_sagemaker.types.model_speculative_decoding_config

        return {
            "ModelSpeculativeDecodingConfig": aws_sdk_sagemaker.types.model_speculative_decoding_config.deserialize_aws_json_1_1(
                data["ModelSpeculativeDecodingConfig"]
            )
        }
    else:
        raise DeserializationError("OptimizationConfig: no recognized variant key")
