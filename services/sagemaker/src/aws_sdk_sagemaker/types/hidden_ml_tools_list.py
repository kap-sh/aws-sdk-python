"""Generated from Smithy shape ``com.amazonaws.sagemaker#HiddenMlToolsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ml_tools

HiddenMlToolsList: TypeAlias = list["aws_sdk_sagemaker.types.ml_tools.MlTools"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HiddenMlToolsList) -> list:
    import aws_sdk_sagemaker.types.ml_tools

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.ml_tools.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> HiddenMlToolsList:
    import aws_sdk_sagemaker.types.ml_tools

    out: HiddenMlToolsList = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.ml_tools.deserialize_aws_json_1_1(item))
    return out
