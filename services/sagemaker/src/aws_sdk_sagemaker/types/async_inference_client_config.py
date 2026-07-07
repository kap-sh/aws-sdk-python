"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncInferenceClientConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_concurrent_invocations_per_instance


class AsyncInferenceClientConfig(TypedDict, closed=True):
    max_concurrent_invocations_per_instance: NotRequired[
        "aws_sdk_sagemaker.types.max_concurrent_invocations_per_instance.MaxConcurrentInvocationsPerInstance"
    ]
    """<p>The maximum number of concurrent requests sent by the SageMaker client to the model container. If no value is provided, SageMaker chooses an optimal value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncInferenceClientConfig) -> dict:
    out: dict = {}
    if "max_concurrent_invocations_per_instance" in value:
        out["MaxConcurrentInvocationsPerInstance"] = value[
            "max_concurrent_invocations_per_instance"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> AsyncInferenceClientConfig:
    out: AsyncInferenceClientConfig = {}  # type: ignore[typeddict-item]
    if "MaxConcurrentInvocationsPerInstance" in data:
        out["max_concurrent_invocations_per_instance"] = data[
            "MaxConcurrentInvocationsPerInstance"
        ]
    return out
