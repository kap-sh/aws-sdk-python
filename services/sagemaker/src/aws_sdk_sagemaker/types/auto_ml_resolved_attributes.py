"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLResolvedAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria
    import aws_sdk_sagemaker.types.auto_ml_job_objective
    import aws_sdk_sagemaker.types.auto_ml_problem_type_resolved_attributes


class AutoMLResolvedAttributes(TypedDict, closed=True):
    auto_ml_job_objective: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_objective.AutoMLJobObjective"
    ]
    completion_criteria: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.AutoMLJobCompletionCriteria"
    ]
    auto_ml_problem_type_resolved_attributes: NotRequired[
        "aws_sdk_sagemaker.types.auto_ml_problem_type_resolved_attributes.AutoMLProblemTypeResolvedAttributes"
    ]
    """<p>Defines the resolved attributes specific to a problem type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLResolvedAttributes) -> dict:
    out: dict = {}
    if "auto_ml_job_objective" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_objective

        out["AutoMLJobObjective"] = (
            aws_sdk_sagemaker.types.auto_ml_job_objective.serialize_aws_json_1_1(
                value["auto_ml_job_objective"]
            )
        )
    if "completion_criteria" in value:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["CompletionCriteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.serialize_aws_json_1_1(
                value["completion_criteria"]
            )
        )
    if "auto_ml_problem_type_resolved_attributes" in value:
        import aws_sdk_sagemaker.types.auto_ml_problem_type_resolved_attributes

        out["AutoMLProblemTypeResolvedAttributes"] = (
            aws_sdk_sagemaker.types.auto_ml_problem_type_resolved_attributes.serialize_aws_json_1_1(
                value["auto_ml_problem_type_resolved_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLResolvedAttributes:
    out: AutoMLResolvedAttributes = {}  # type: ignore[typeddict-item]
    if "AutoMLJobObjective" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_objective

        out["auto_ml_job_objective"] = (
            aws_sdk_sagemaker.types.auto_ml_job_objective.deserialize_aws_json_1_1(
                data["AutoMLJobObjective"]
            )
        )
    if "CompletionCriteria" in data:
        import aws_sdk_sagemaker.types.auto_ml_job_completion_criteria

        out["completion_criteria"] = (
            aws_sdk_sagemaker.types.auto_ml_job_completion_criteria.deserialize_aws_json_1_1(
                data["CompletionCriteria"]
            )
        )
    if "AutoMLProblemTypeResolvedAttributes" in data:
        import aws_sdk_sagemaker.types.auto_ml_problem_type_resolved_attributes

        out["auto_ml_problem_type_resolved_attributes"] = (
            aws_sdk_sagemaker.types.auto_ml_problem_type_resolved_attributes.deserialize_aws_json_1_1(
                data["AutoMLProblemTypeResolvedAttributes"]
            )
        )
    return out
