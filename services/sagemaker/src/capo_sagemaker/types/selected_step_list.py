"""Generated from Smithy shape ``com.amazonaws.sagemaker#SelectedStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.selected_step

SelectedStepList: TypeAlias = list["capo_sagemaker.types.selected_step.SelectedStep"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectedStepList) -> list:
    import capo_sagemaker.types.selected_step

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.selected_step.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SelectedStepList:
    import capo_sagemaker.types.selected_step

    out: SelectedStepList = []
    for item in data:
        out.append(capo_sagemaker.types.selected_step.deserialize_aws_json_1_1(item))
    return out
