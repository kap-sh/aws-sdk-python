"""Generated from Smithy shape ``com.amazonaws.sagemaker#CandidateSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_candidate_step

CandidateSteps: TypeAlias = list[
    "capo_sagemaker.types.auto_ml_candidate_step.AutoMLCandidateStep"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CandidateSteps) -> list:
    import capo_sagemaker.types.auto_ml_candidate_step

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.auto_ml_candidate_step.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CandidateSteps:
    import capo_sagemaker.types.auto_ml_candidate_step

    out: CandidateSteps = []
    for item in data:
        out.append(
            capo_sagemaker.types.auto_ml_candidate_step.deserialize_aws_json_1_1(item)
        )
    return out
