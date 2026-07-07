"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateLabelingJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.labeling_job_arn


class CreateLabelingJobResponse(TypedDict, closed=True):
    labeling_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.labeling_job_arn.LabelingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the labeling job. You use this ARN to identify the labeling job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLabelingJobResponse) -> dict:
    out: dict = {}
    if "labeling_job_arn" in value:
        out["LabelingJobArn"] = value["labeling_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLabelingJobResponse:
    out: CreateLabelingJobResponse = {}  # type: ignore[typeddict-item]
    if "LabelingJobArn" in data:
        out["labeling_job_arn"] = data["LabelingJobArn"]
    return out
