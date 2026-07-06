"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExperimentSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.experiment_source_arn
    import aws_sdk_sagemaker.types.source_type


class ExperimentSource(TypedDict, closed=True):
    source_arn: NotRequired[
        "aws_sdk_sagemaker.types.experiment_source_arn.ExperimentSourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source.</p>"""
    source_type: NotRequired["aws_sdk_sagemaker.types.source_type.SourceType"]
    """<p>The source type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperimentSource) -> dict:
    out: dict = {}
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "source_type" in value:
        out["SourceType"] = value["source_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperimentSource:
    out: ExperimentSource = {}  # type: ignore[typeddict-item]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "SourceType" in data:
        out["source_type"] = data["SourceType"]
    return out
