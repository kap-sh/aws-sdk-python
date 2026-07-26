"""Generated from Smithy shape ``com.amazonaws.sagemaker#Workteams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.workteam

Workteams: TypeAlias = list["capo_sagemaker.types.workteam.Workteam"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workteams) -> list:
    import capo_sagemaker.types.workteam

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.workteam.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Workteams:
    import capo_sagemaker.types.workteam

    out: Workteams = []
    for item in data:
        out.append(capo_sagemaker.types.workteam.deserialize_aws_json_1_1(item))
    return out
