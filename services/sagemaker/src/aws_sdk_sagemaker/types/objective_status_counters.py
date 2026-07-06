"""Generated from Smithy shape ``com.amazonaws.sagemaker#ObjectiveStatusCounters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.objective_status_counter


class ObjectiveStatusCounters(TypedDict, closed=True):
    succeeded: NotRequired[
        "aws_sdk_sagemaker.types.objective_status_counter.ObjectiveStatusCounter"
    ]
    """<p>The number of training jobs whose final objective metric was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.</p>"""
    pending: NotRequired[
        "aws_sdk_sagemaker.types.objective_status_counter.ObjectiveStatusCounter"
    ]
    """<p>The number of training jobs that are in progress and pending evaluation of their final objective metric.</p>"""
    failed: NotRequired[
        "aws_sdk_sagemaker.types.objective_status_counter.ObjectiveStatusCounter"
    ]
    """<p>The number of training jobs whose final objective metric was not evaluated and used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectiveStatusCounters) -> dict:
    out: dict = {}
    if "succeeded" in value:
        out["Succeeded"] = value["succeeded"]
    if "pending" in value:
        out["Pending"] = value["pending"]
    if "failed" in value:
        out["Failed"] = value["failed"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ObjectiveStatusCounters:
    out: ObjectiveStatusCounters = {}  # type: ignore[typeddict-item]
    if "Succeeded" in data:
        out["succeeded"] = data["Succeeded"]
    if "Pending" in data:
        out["pending"] = data["Pending"]
    if "Failed" in data:
        out["failed"] = data["Failed"]
    return out
