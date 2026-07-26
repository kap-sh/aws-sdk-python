"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobOutputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.model_invocation_job_s3_output_data_config


class _ModelInvocationJobOutputDataConfig_s3OutputDataConfig(TypedDict, closed=True):
    s3OutputDataConfig: "capo_bedrock.types.model_invocation_job_s3_output_data_config.ModelInvocationJobS3OutputDataConfig"


ModelInvocationJobOutputDataConfig: TypeAlias = (
    _ModelInvocationJobOutputDataConfig_s3OutputDataConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobOutputDataConfig) -> dict:
    if "s3OutputDataConfig" in value:
        import capo_bedrock.types.model_invocation_job_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock.types.model_invocation_job_s3_output_data_config.serialize_json(
                value["s3OutputDataConfig"]
            )
        }
    else:
        raise SerializationError(
            "ModelInvocationJobOutputDataConfig: no variant present"
        )


def deserialize_json(data: dict) -> ModelInvocationJobOutputDataConfig:
    if "s3OutputDataConfig" in data:
        import capo_bedrock.types.model_invocation_job_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock.types.model_invocation_job_s3_output_data_config.deserialize_json(
                data["s3OutputDataConfig"]
            )
        }
    else:
        raise DeserializationError(
            "ModelInvocationJobOutputDataConfig: no recognized variant key"
        )
