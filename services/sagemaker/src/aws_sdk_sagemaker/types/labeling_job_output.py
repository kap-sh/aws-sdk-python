"""Generated from Smithy shape ``com.amazonaws.sagemaker#LabelingJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_arn
    import aws_sdk_sagemaker.types.s3_uri


class LabelingJobOutput(TypedDict, closed=True):
    output_dataset_s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 bucket location of the manifest file for labeled data. </p>"""
    final_active_learning_model_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_arn.ModelArn"
    ]
    """<p>The Amazon Resource Name (ARN) for the most recent SageMaker model trained as part of automated data labeling. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelingJobOutput) -> dict:
    out: dict = {}
    if "output_dataset_s3_uri" in value:
        out["OutputDatasetS3Uri"] = value["output_dataset_s3_uri"]
    if "final_active_learning_model_arn" in value:
        out["FinalActiveLearningModelArn"] = value["final_active_learning_model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelingJobOutput:
    out: LabelingJobOutput = {}  # type: ignore[typeddict-item]
    if "OutputDatasetS3Uri" in data:
        out["output_dataset_s3_uri"] = data["OutputDatasetS3Uri"]
    if "FinalActiveLearningModelArn" in data:
        out["final_active_learning_model_arn"] = data["FinalActiveLearningModelArn"]
    return out
