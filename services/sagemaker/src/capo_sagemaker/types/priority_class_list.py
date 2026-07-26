"""Generated from Smithy shape ``com.amazonaws.sagemaker#PriorityClassList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.priority_class

PriorityClassList: TypeAlias = list["capo_sagemaker.types.priority_class.PriorityClass"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriorityClassList) -> list:
    import capo_sagemaker.types.priority_class

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.priority_class.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PriorityClassList:
    import capo_sagemaker.types.priority_class

    out: PriorityClassList = []
    for item in data:
        out.append(capo_sagemaker.types.priority_class.deserialize_aws_json_1_1(item))
    return out
