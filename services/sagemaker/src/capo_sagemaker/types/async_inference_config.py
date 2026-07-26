"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncInferenceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.async_inference_client_config
    import capo_sagemaker.types.async_inference_output_config


class AsyncInferenceConfig(TypedDict, closed=True):
    client_config: NotRequired[
        "capo_sagemaker.types.async_inference_client_config.AsyncInferenceClientConfig"
    ]
    """<p>Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.async_inference_output_config.AsyncInferenceOutputConfig"
    ]
    """<p>Specifies the configuration for asynchronous inference invocation outputs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncInferenceConfig) -> dict:
    out: dict = {}
    if "client_config" in value:
        import capo_sagemaker.types.async_inference_client_config

        out["ClientConfig"] = (
            capo_sagemaker.types.async_inference_client_config.serialize_aws_json_1_1(
                value["client_config"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.async_inference_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.async_inference_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AsyncInferenceConfig:
    out: AsyncInferenceConfig = {}  # type: ignore[typeddict-item]
    if "ClientConfig" in data:
        import capo_sagemaker.types.async_inference_client_config

        out["client_config"] = (
            capo_sagemaker.types.async_inference_client_config.deserialize_aws_json_1_1(
                data["ClientConfig"]
            )
        )
    if "OutputConfig" in data:
        import capo_sagemaker.types.async_inference_output_config

        out["output_config"] = (
            capo_sagemaker.types.async_inference_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    return out
