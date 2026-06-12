"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLCandidates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_candidate

AutoMLCandidates: TypeAlias = list[
    "aws_sdk_sagemaker.types.auto_ml_candidate.AutoMLCandidate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLCandidates) -> list:
    import aws_sdk_sagemaker.types.auto_ml_candidate

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_candidate.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLCandidates:
    import aws_sdk_sagemaker.types.auto_ml_candidate

    out: AutoMLCandidates = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_candidate.deserialize_aws_json_1_1(item)
        )
    return out
