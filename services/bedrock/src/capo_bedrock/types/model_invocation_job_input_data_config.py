"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationJobInputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.model_invocation_job_s3_input_data_config


class _ModelInvocationJobInputDataConfig_s3InputDataConfig(TypedDict, closed=True):
    s3InputDataConfig: "capo_bedrock.types.model_invocation_job_s3_input_data_config.ModelInvocationJobS3InputDataConfig"


ModelInvocationJobInputDataConfig: TypeAlias = (
    _ModelInvocationJobInputDataConfig_s3InputDataConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: ModelInvocationJobInputDataConfig) -> dict:
    if "s3InputDataConfig" in value:
        import capo_bedrock.types.model_invocation_job_s3_input_data_config

        return {
            "s3InputDataConfig": capo_bedrock.types.model_invocation_job_s3_input_data_config.serialize_json(
                value["s3InputDataConfig"]
            )
        }
    else:
        raise SerializationError(
            "ModelInvocationJobInputDataConfig: no variant present"
        )


def deserialize_json(data: dict) -> ModelInvocationJobInputDataConfig:
    if data.get("s3InputDataConfig") is not None:
        import capo_bedrock.types.model_invocation_job_s3_input_data_config

        return {
            "s3InputDataConfig": capo_bedrock.types.model_invocation_job_s3_input_data_config.deserialize_json(
                data["s3InputDataConfig"]
            )
        }
    else:
        raise DeserializationError(
            "ModelInvocationJobInputDataConfig: no recognized variant key"
        )
