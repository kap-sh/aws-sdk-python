"""Generated from Smithy shape ``com.amazonaws.sagemaker#TextClassificationJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria
    import aws_sdk_sagemaker.types.content_column
    import aws_sdk_sagemaker.types.target_label_column


class TextClassificationJobConfig(TypedDict, closed=True):
    completion_criteria: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]
    """<p>How long a job is allowed to run, or how many candidates a job is allowed to generate.</p>"""
    content_column: NotRequired["aws_sdk_sagemaker.types.content_column.ContentColumn"]
    """<p>The name of the column used to provide the sentences to be classified. It should not be the same as the target column.</p>"""
    target_label_column: NotRequired[
        "aws_sdk_sagemaker.types.target_label_column.TargetLabelColumn"
    ]
    """<p>The name of the column used to provide the class labels. It should not be same as the content column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextClassificationJobConfig) -> dict:
    out: dict = {}
    if "completion_criteria" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    if "content_column" in value:
        out["ContentColumn"] = value["content_column"]
    if "target_label_column" in value:
        out["TargetLabelColumn"] = value["target_label_column"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TextClassificationJobConfig:
    out: TextClassificationJobConfig = {}  # type: ignore[typeddict-item]
    if "CompletionCriteria" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    if "ContentColumn" in data:
        out["content_column"] = data["ContentColumn"]
    if "TargetLabelColumn" in data:
        out["target_label_column"] = data["TargetLabelColumn"]
    return out
