"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLInputDataConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_channel

AutoMLInputDataConfig: TypeAlias = list[
    "aws_sdk_sagemaker.types.auto_ml_channel.AutoMLChannel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLInputDataConfig) -> list:
    import aws_sdk_sagemaker.types.auto_ml_channel

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.auto_ml_channel.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLInputDataConfig:
    import aws_sdk_sagemaker.types.auto_ml_channel

    out: AutoMLInputDataConfig = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_channel.deserialize_aws_json_1_1(item)
        )
    return out
