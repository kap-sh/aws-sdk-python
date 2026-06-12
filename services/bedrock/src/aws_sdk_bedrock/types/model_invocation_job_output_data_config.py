"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobOutputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_invocation_job_s3_output_data_config


class _ModelInvocationJobOutputDataConfig_s3OutputDataConfig(TypedDict):
    s3OutputDataConfig: "aws_sdk_bedrock.types.model_invocation_job_s3_output_data_config.ModelInvocationJobS3OutputDataConfig"


ModelInvocationJobOutputDataConfig: TypeAlias = (
    _ModelInvocationJobOutputDataConfig_s3OutputDataConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobOutputDataConfig) -> dict:
    if "s3OutputDataConfig" in value:
        import aws_sdk_bedrock.types.model_invocation_job_s3_output_data_config

        return {
            "s3OutputDataConfig": aws_sdk_bedrock.types.model_invocation_job_s3_output_data_config.serialize_json(
                value["s3OutputDataConfig"]
            )
        }
    else:
        raise SerializationError(
            "ModelInvocationJobOutputDataConfig: no variant present"
        )


def deserialize_json(data: dict) -> ModelInvocationJobOutputDataConfig:
    if "s3OutputDataConfig" in data:
        import aws_sdk_bedrock.types.model_invocation_job_s3_output_data_config

        return {
            "s3OutputDataConfig": aws_sdk_bedrock.types.model_invocation_job_s3_output_data_config.deserialize_json(
                data["s3OutputDataConfig"]
            )
        }
    else:
        raise DeserializationError(
            "ModelInvocationJobOutputDataConfig: no recognized variant key"
        )
