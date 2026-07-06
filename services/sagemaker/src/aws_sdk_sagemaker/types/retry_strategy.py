"""Generated from Smithy shape ``com.amazonaws.sagemaker#RetryStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.maximum_retry_attempts


class RetryStrategy(TypedDict, closed=True):
    maximum_retry_attempts: NotRequired[
        "aws_sdk_sagemaker.types.maximum_retry_attempts.MaximumRetryAttempts"
    ]
    """<p>The number of times to retry the job. When the job is retried, it's <code>SecondaryStatus</code> is changed to <code>STARTING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetryStrategy) -> dict:
    out: dict = {}
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetryStrategy:
    out: RetryStrategy = {}  # type: ignore[typeddict-item]
    if "MaximumRetryAttempts" in data:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    return out
