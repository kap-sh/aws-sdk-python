"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncInferenceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.async_inference_client_config
    import aws_sdk_sagemaker.types.async_inference_output_config


class AsyncInferenceConfig(TypedDict):
    client_config: NotRequired[
        "aws_sdk_sagemaker.types.async_inference_client_config.AsyncInferenceClientConfig"
    ]
    """<p>Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.async_inference_output_config.AsyncInferenceOutputConfig"
    ]
    """<p>Specifies the configuration for asynchronous inference invocation outputs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncInferenceConfig) -> dict:
    out: dict = {}
    if "client_config" in value:
        import aws_sdk_sagemaker.types.async_inference_client_config

        out["ClientConfig"] = (
            aws_sdk_sagemaker.types.async_inference_client_config.serialize_aws_json_1_1(
                value["client_config"]
            )
        )
    if "output_config" in value:
        import aws_sdk_sagemaker.types.async_inference_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.async_inference_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AsyncInferenceConfig:
    out: AsyncInferenceConfig = {}  # type: ignore[typeddict-item]
    if "ClientConfig" in data:
        import aws_sdk_sagemaker.types.async_inference_client_config

        out["client_config"] = (
            aws_sdk_sagemaker.types.async_inference_client_config.deserialize_aws_json_1_1(
                data["ClientConfig"]
            )
        )
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.async_inference_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.async_inference_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    return out
