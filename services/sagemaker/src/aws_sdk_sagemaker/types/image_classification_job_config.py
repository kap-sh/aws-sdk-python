"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageClassificationJobConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria


class ImageClassificationJobConfig(TypedDict, closed=True):
    completion_criteria: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]
    """<p>How long a job is allowed to run, or how many candidates a job is allowed to generate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageClassificationJobConfig) -> dict:
    out: dict = {}
    if "completion_criteria" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageClassificationJobConfig:
    out: ImageClassificationJobConfig = {}  # type: ignore[typeddict-item]
    if "CompletionCriteria" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    return out
