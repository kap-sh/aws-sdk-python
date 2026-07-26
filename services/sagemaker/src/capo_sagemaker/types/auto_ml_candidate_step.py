"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLCandidateStep``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.candidate_step_arn
    import capo_sagemaker.types.candidate_step_name
    import capo_sagemaker.types.candidate_step_type


class AutoMLCandidateStep(TypedDict, closed=True):
    candidate_step_type: NotRequired[
        "capo_sagemaker.types.candidate_step_type.CandidateStepType"
    ]
    """<p>Whether the candidate is at the transform, training, or processing step.</p>"""
    candidate_step_arn: NotRequired[
        "capo_sagemaker.types.candidate_step_arn.CandidateStepArn"
    ]
    """<p>The ARN for the candidate's step.</p>"""
    candidate_step_name: NotRequired[
        "capo_sagemaker.types.candidate_step_name.CandidateStepName"
    ]
    """<p>The name for the candidate's step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLCandidateStep) -> dict:
    out: dict = {}
    if "candidate_step_type" in value:
        import capo_sagemaker.types.candidate_step_type

        out["CandidateStepType"] = (
            capo_sagemaker.types.candidate_step_type.serialize_aws_json_1_1(
                value["candidate_step_type"]
            )
        )
    if "candidate_step_arn" in value:
        out["CandidateStepArn"] = value["candidate_step_arn"]
    if "candidate_step_name" in value:
        out["CandidateStepName"] = value["candidate_step_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoMLCandidateStep:
    out: AutoMLCandidateStep = {}  # type: ignore[typeddict-item]
    if "CandidateStepType" in data:
        import capo_sagemaker.types.candidate_step_type

        out["candidate_step_type"] = (
            capo_sagemaker.types.candidate_step_type.deserialize_aws_json_1_1(
                data["CandidateStepType"]
            )
        )
    if "CandidateStepArn" in data:
        out["candidate_step_arn"] = data["CandidateStepArn"]
    if "CandidateStepName" in data:
        out["candidate_step_name"] = data["CandidateStepName"]
    return out
