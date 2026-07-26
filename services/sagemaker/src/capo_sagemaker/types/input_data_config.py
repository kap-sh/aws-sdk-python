"""Generated from Smithy shape ``com.amazonaws.sagemaker#InputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.channel

InputDataConfig: TypeAlias = list["capo_sagemaker.types.channel.Channel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputDataConfig) -> list:
    import capo_sagemaker.types.channel

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.channel.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InputDataConfig:
    import capo_sagemaker.types.channel

    out: InputDataConfig = []
    for item in data:
        out.append(capo_sagemaker.types.channel.deserialize_aws_json_1_1(item))
    return out
