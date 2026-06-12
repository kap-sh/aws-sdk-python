"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobInputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_invocation_job_s3_input_data_config


class _ModelInvocationJobInputDataConfig_s3InputDataConfig(TypedDict):
    s3InputDataConfig: "aws_sdk_bedrock.types.model_invocation_job_s3_input_data_config.ModelInvocationJobS3InputDataConfig"


ModelInvocationJobInputDataConfig: TypeAlias = (
    _ModelInvocationJobInputDataConfig_s3InputDataConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobInputDataConfig) -> dict:
    if "s3InputDataConfig" in value:
        import aws_sdk_bedrock.types.model_invocation_job_s3_input_data_config

        return {
            "s3InputDataConfig": aws_sdk_bedrock.types.model_invocation_job_s3_input_data_config.serialize_json(
                value["s3InputDataConfig"]
            )
        }
    else:
        raise SerializationError(
            "ModelInvocationJobInputDataConfig: no variant present"
        )


def deserialize_json(data: dict) -> ModelInvocationJobInputDataConfig:
    if "s3InputDataConfig" in data:
        import aws_sdk_bedrock.types.model_invocation_job_s3_input_data_config

        return {
            "s3InputDataConfig": aws_sdk_bedrock.types.model_invocation_job_s3_input_data_config.deserialize_json(
                data["s3InputDataConfig"]
            )
        }
    else:
        raise DeserializationError(
            "ModelInvocationJobInputDataConfig: no recognized variant key"
        )
