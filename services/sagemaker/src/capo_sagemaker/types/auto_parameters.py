"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_parameter

AutoParameters: TypeAlias = list["capo_sagemaker.types.auto_parameter.AutoParameter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoParameters) -> list:
    import capo_sagemaker.types.auto_parameter

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.auto_parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AutoParameters:
    import capo_sagemaker.types.auto_parameter

    out: AutoParameters = []
    for item in data:
        out.append(capo_sagemaker.types.auto_parameter.deserialize_aws_json_1_1(item))
    return out
