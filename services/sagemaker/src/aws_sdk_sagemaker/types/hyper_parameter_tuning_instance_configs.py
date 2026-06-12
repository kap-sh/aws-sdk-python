"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningInstanceConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_instance_config

HyperParameterTuningInstanceConfigs: TypeAlias = list[
    "aws_sdk_sagemaker.types.hyper_parameter_tuning_instance_config.HyperParameterTuningInstanceConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningInstanceConfigs) -> list:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_instance_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.hyper_parameter_tuning_instance_config.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HyperParameterTuningInstanceConfigs:
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_instance_config

    out: HyperParameterTuningInstanceConfigs = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.hyper_parameter_tuning_instance_config.deserialize_aws_json_1_1(
                item
            )
        )
    return out
