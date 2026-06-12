"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLCandidateStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.candidate_step_arn
    import aws_sdk_sagemaker.types.candidate_step_name
    import aws_sdk_sagemaker.types.candidate_step_type


class AutoMLCandidateStep(TypedDict):
    candidate_step_type: NotRequired[
        "aws_sdk_sagemaker.types.candidate_step_type.CandidateStepType"
    ]
    """<p>Whether the candidate is at the transform, training, or processing step.</p>"""
    candidate_step_arn: NotRequired[
        "aws_sdk_sagemaker.types.candidate_step_arn.CandidateStepArn"
    ]
    """<p>The ARN for the candidate's step.</p>"""
    candidate_step_name: NotRequired[
        "aws_sdk_sagemaker.types.candidate_step_name.CandidateStepName"
    ]
    """<p>The name for the candidate's step.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLCandidateStep) -> dict:
    out: dict = {}
    if "candidate_step_type" in value:
        import aws_sdk_sagemaker.types.candidate_step_type

        out["CandidateStepType"] = (
            aws_sdk_sagemaker.types.candidate_step_type.serialize_aws_json_1_1(
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
        import aws_sdk_sagemaker.types.candidate_step_type

        out["candidate_step_type"] = (
            aws_sdk_sagemaker.types.candidate_step_type.deserialize_aws_json_1_1(
                data["CandidateStepType"]
            )
        )
    if "CandidateStepArn" in data:
        out["candidate_step_arn"] = data["CandidateStepArn"]
    if "CandidateStepName" in data:
        out["candidate_step_name"] = data["CandidateStepName"]
    return out
