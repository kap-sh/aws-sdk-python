"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelCounters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.label_counter


class LabelCounters(TypedDict, closed=True):
    total_labeled: NotRequired["aws_sdk_sagemaker.types.label_counter.LabelCounter"]
    """<p>The total number of objects labeled.</p>"""
    human_labeled: NotRequired["aws_sdk_sagemaker.types.label_counter.LabelCounter"]
    """<p>The total number of objects labeled by a human worker.</p>"""
    machine_labeled: NotRequired["aws_sdk_sagemaker.types.label_counter.LabelCounter"]
    """<p>The total number of objects labeled by automated data labeling.</p>"""
    failed_non_retryable_error: NotRequired[
        "aws_sdk_sagemaker.types.label_counter.LabelCounter"
    ]
    """<p>The total number of objects that could not be labeled due to an error.</p>"""
    unlabeled: NotRequired["aws_sdk_sagemaker.types.label_counter.LabelCounter"]
    """<p>The total number of objects not yet labeled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelCounters) -> dict:
    out: dict = {}
    if "total_labeled" in value:
        out["TotalLabeled"] = value["total_labeled"]
    if "human_labeled" in value:
        out["HumanLabeled"] = value["human_labeled"]
    if "machine_labeled" in value:
        out["MachineLabeled"] = value["machine_labeled"]
    if "failed_non_retryable_error" in value:
        out["FailedNonRetryableError"] = value["failed_non_retryable_error"]
    if "unlabeled" in value:
        out["Unlabeled"] = value["unlabeled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelCounters:
    out: LabelCounters = {}  # type: ignore[typeddict-item]
    if "TotalLabeled" in data:
        out["total_labeled"] = data["TotalLabeled"]
    if "HumanLabeled" in data:
        out["human_labeled"] = data["HumanLabeled"]
    if "MachineLabeled" in data:
        out["machine_labeled"] = data["MachineLabeled"]
    if "FailedNonRetryableError" in data:
        out["failed_non_retryable_error"] = data["FailedNonRetryableError"]
    if "Unlabeled" in data:
        out["unlabeled"] = data["Unlabeled"]
    return out
