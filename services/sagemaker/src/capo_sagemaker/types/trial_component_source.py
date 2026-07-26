"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.source_type
    import capo_sagemaker.types.trial_component_source_arn


class TrialComponentSource(TypedDict, closed=True):
    source_arn: NotRequired[
        "capo_sagemaker.types.trial_component_source_arn.TrialComponentSourceArn"
    ]
    """<p>The source Amazon Resource Name (ARN).</p>"""
    source_type: NotRequired["capo_sagemaker.types.source_type.SourceType"]
    """<p>The source job type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentSource) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrialComponentSource:
    out: TrialComponentSource = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    return out
