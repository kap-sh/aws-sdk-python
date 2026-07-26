"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.source_type
    import capo_sagemaker.types.trial_source_arn


class TrialSource(TypedDict, closed=True):
    source_arn: NotRequired["capo_sagemaker.types.trial_source_arn.TrialSourceArn"]
    """<p>The Amazon Resource Name (ARN) of the source.</p>"""
    source_type: NotRequired["capo_sagemaker.types.source_type.SourceType"]
    """<p>The source job type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialSource) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialSource:
    out: TrialSource = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    return out
