"""Generated from Smithy shape ``com.amazonaws.sagemaker#Parents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.parent

Parents: TypeAlias = list["capo_sagemaker.types.parent.Parent"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Parents) -> list:
    import capo_sagemaker.types.parent

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.parent.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Parents:
    import capo_sagemaker.types.parent

    out: Parents = []
    for item in data:
        out.append(capo_sagemaker.types.parent.deserialize_aws_json_1_1(item))
    return out
