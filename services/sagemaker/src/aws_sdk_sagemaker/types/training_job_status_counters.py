"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobStatusCounters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_job_status_counter


class TrainingJobStatusCounters(TypedDict):
    completed: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status_counter.TrainingJobStatusCounter"
    ]
    """<p>The number of completed training jobs launched by the hyperparameter tuning job.</p>"""
    in_progress: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status_counter.TrainingJobStatusCounter"
    ]
    """<p>The number of in-progress training jobs launched by a hyperparameter tuning job.</p>"""
    retryable_error: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status_counter.TrainingJobStatusCounter"
    ]
    """<p>The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.</p>"""
    non_retryable_error: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status_counter.TrainingJobStatusCounter"
    ]
    """<p>The number of training jobs that failed and can't be retried. A failed training job can't be retried if it failed because a client error occurred.</p>"""
    stopped: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status_counter.TrainingJobStatusCounter"
    ]
    """<p>The number of training jobs launched by a hyperparameter tuning job that were manually stopped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJobStatusCounters) -> dict:
    out: dict = {}
    if "completed" in value:
        out["Completed"] = value["completed"]
    if "in_progress" in value:
        out["InProgress"] = value["in_progress"]
    if "retryable_error" in value:
        out["RetryableError"] = value["retryable_error"]
    if "non_retryable_error" in value:
        out["NonRetryableError"] = value["non_retryable_error"]
    if "stopped" in value:
        out["Stopped"] = value["stopped"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingJobStatusCounters:
    out: TrainingJobStatusCounters = {}  # type: ignore[typeddict-item]
    if "Completed" in data:
        out["completed"] = data["Completed"]
    if "InProgress" in data:
        out["in_progress"] = data["InProgress"]
    if "RetryableError" in data:
        out["retryable_error"] = data["RetryableError"]
    if "NonRetryableError" in data:
        out["non_retryable_error"] = data["NonRetryableError"]
    if "Stopped" in data:
        out["stopped"] = data["Stopped"]
    return out
