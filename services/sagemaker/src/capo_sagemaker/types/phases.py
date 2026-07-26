"""Generated from Smithy shape ``com.amazonaws.sagemaker#Phases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.phase

Phases: TypeAlias = list["capo_sagemaker.types.phase.Phase"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Phases) -> list:
    import capo_sagemaker.types.phase

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.phase.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Phases:
    import capo_sagemaker.types.phase

    out: Phases = []
    for item in data:
        out.append(capo_sagemaker.types.phase.deserialize_aws_json_1_1(item))
    return out
