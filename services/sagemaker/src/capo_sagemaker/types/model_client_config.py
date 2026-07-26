"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelClientConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.invocations_max_retries
    import capo_sagemaker.types.invocations_timeout_in_seconds


class ModelClientConfig(TypedDict, closed=True):
    invocations_timeout_in_seconds: NotRequired[
        "capo_sagemaker.types.invocations_timeout_in_seconds.InvocationsTimeoutInSeconds"
    ]
    """<p>The timeout value in seconds for an invocation request. The default value is 600.</p>"""
    invocations_max_retries: NotRequired[
        "capo_sagemaker.types.invocations_max_retries.InvocationsMaxRetries"
    ]
    """<p>The maximum number of retries when invocation requests are failing. The default value is 3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelClientConfig) -> dict:
    out: dict = {}
    if "invocations_timeout_in_seconds" in value:
        out["InvocationsTimeoutInSeconds"] = value["invocations_timeout_in_seconds"]
    if "invocations_max_retries" in value:
        out["InvocationsMaxRetries"] = value["invocations_max_retries"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelClientConfig:
    out: ModelClientConfig = {}  # type: ignore[typeddict-item]
    if "InvocationsTimeoutInSeconds" in data:
        out["invocations_timeout_in_seconds"] = data["InvocationsTimeoutInSeconds"]
    if "InvocationsMaxRetries" in data:
        out["invocations_max_retries"] = data["InvocationsMaxRetries"]
    return out
