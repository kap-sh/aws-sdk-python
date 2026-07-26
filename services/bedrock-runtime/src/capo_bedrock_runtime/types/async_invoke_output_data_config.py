"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeOutputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.async_invoke_s3_output_data_config


class _AsyncInvokeOutputDataConfig_s3OutputDataConfig(TypedDict, closed=True):
    s3OutputDataConfig: "capo_bedrock_runtime.types.async_invoke_s3_output_data_config.AsyncInvokeS3OutputDataConfig"


AsyncInvokeOutputDataConfig: TypeAlias = _AsyncInvokeOutputDataConfig_s3OutputDataConfig


# --- restJson1 ser/de ---
def serialize_json(value: AsyncInvokeOutputDataConfig) -> dict:
    if "s3OutputDataConfig" in value:
        import capo_bedrock_runtime.types.async_invoke_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock_runtime.types.async_invoke_s3_output_data_config.serialize_json(
                value["s3OutputDataConfig"]
            )
        }
    else:
        raise SerializationError("AsyncInvokeOutputDataConfig: no variant present")


def deserialize_json(data: dict) -> AsyncInvokeOutputDataConfig:
    if "s3OutputDataConfig" in data:
        import capo_bedrock_runtime.types.async_invoke_s3_output_data_config

        return {
            "s3OutputDataConfig": capo_bedrock_runtime.types.async_invoke_s3_output_data_config.deserialize_json(
                data["s3OutputDataConfig"]
            )
        }
    else:
        raise DeserializationError(
            "AsyncInvokeOutputDataConfig: no recognized variant key"
        )
