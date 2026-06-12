"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResolvedAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria
    import aws_sdk_sagemaker.types.auto_ml_job_objective
    import aws_sdk_sagemaker.types.problem_type


class ResolvedAttributes(TypedDict):
    auto_ml_job_objective: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_objective.AutoMLJobObjective"
    ]
    problem_type: NotRequired["aws_sdk_sagemaker.types.problem_type.ProblemType"]
    """<p>The problem type.</p>"""
    completion_criteria: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedAttributes) -> dict:
    out: dict = {}
    if "auto_ml_job_objective" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_objective

        out["AutoMLJobObjective"] = (
            aws_sdk_sagemaker.types.auto_ml_job_objective.serialize_aws_json_1_1(
                value["auto_ml_job_objective"]
            )
        )
    if "problem_type" in value:
        import aws_sdk_sagemaker.types.problem_type

        out["ProblemType"] = (
            aws_sdk_sagemaker.types.problem_type.serialize_aws_json_1_1(
                value["problem_type"]
            )
        )
    if "completion_criteria" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedAttributes:
    out: ResolvedAttributes = {}  # type: ignore[typeddict-item]
    if "AutoMLJobObjective" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_objective

        out["auto_ml_job_objective"] = (
            aws_sdk_sagemaker.types.auto_ml_job_objective.deserialize_aws_json_1_1(
                data["AutoMLJobObjective"]
            )
        )
    if "ProblemType" in data:
        import aws_sdk_sagemaker.types.problem_type

        out["problem_type"] = (
            aws_sdk_sagemaker.types.problem_type.deserialize_aws_json_1_1(
                data["ProblemType"]
            )
        )
    if "CompletionCriteria" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    return out
