"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLCandidates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_candidate

AutoMLCandidates: TypeAlias = list[
    "capo_sagemaker.types.auto_ml_candidate.AutoMLCandidate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLCandidates) -> list:
    import capo_sagemaker.types.auto_ml_candidate

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.auto_ml_candidate.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLCandidates:
    import capo_sagemaker.types.auto_ml_candidate

    out: AutoMLCandidates = []
    for item in data:
        out.append(
            capo_sagemaker.types.auto_ml_candidate.deserialize_aws_json_1_1(item)
        )
    return out
