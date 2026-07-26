"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResolvedAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_job_completion_criteria
    import capo_sagemaker.types.auto_ml_job_objective
    import capo_sagemaker.types.problem_type


class ResolvedAttributes(TypedDict, closed=True):
    auto_ml_job_objective: NotRequired[
        "capo_sagemaker.types.auto_ml_job_objective.AutoMLJobObjective"
    ]
    problem_type: NotRequired["capo_sagemaker.types.problem_type.ProblemType"]
    """<p>The problem type.</p>"""
    completion_criteria: NotRequired[
        "capo_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedAttributes) -> dict:
    out: dict = {}
    if "auto_ml_job_objective" in value:
        import capo_sagemaker.types.auto_ml_job_objective

        out["AutoMLJobObjective"] = (
            capo_sagemaker.types.auto_ml_job_objective.serialize_aws_json_1_1(
                value["auto_ml_job_objective"]
            )
        )
    if "problem_type" in value:
        import capo_sagemaker.types.problem_type

        out["ProblemType"] = capo_sagemaker.types.problem_type.serialize_aws_json_1_1(
            value["problem_type"]
        )
    if "completion_criteria" in value:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolvedAttributes:
    out: ResolvedAttributes = {}  # type: ignore[typeddict-item]
    if "AutoMLJobObjective" in data:
        import capo_sagemaker.types.auto_ml_job_objective

        out["auto_ml_job_objective"] = (
            capo_sagemaker.types.auto_ml_job_objective.deserialize_aws_json_1_1(
                data["AutoMLJobObjective"]
            )
        )
    if "ProblemType" in data:
        import capo_sagemaker.types.problem_type

        out["problem_type"] = (
            capo_sagemaker.types.problem_type.deserialize_aws_json_1_1(
                data["ProblemType"]
            )
        )
    if "CompletionCriteria" in data:
        import capo_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            capo_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    return out
