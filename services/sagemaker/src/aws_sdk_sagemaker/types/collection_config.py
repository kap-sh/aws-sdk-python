"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.vector_config


class _CollectionConfig_VectorConfig(TypedDict):
    VectorConfig: "aws_sdk_sagemaker.types.vector_config.VectorConfig"


CollectionConfig: TypeAlias = _CollectionConfig_VectorConfig


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectionConfig) -> dict:
    if "VectorConfig" in value:
        import aws_sdk_sagemaker.types.vector_config

        return {
            "VectorConfig": aws_sdk_sagemaker.types.vector_config.serialize_aws_json_1_1(
                value["VectorConfig"]
            )
        }
    else:
        raise SerializationError("CollectionConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CollectionConfig:
    if "VectorConfig" in data:
        import aws_sdk_sagemaker.types.vector_config

        return {
            "VectorConfig": aws_sdk_sagemaker.types.vector_config.deserialize_aws_json_1_1(
                data["VectorConfig"]
            )
        }
    else:
        raise DeserializationError("CollectionConfig: no recognized variant key")
