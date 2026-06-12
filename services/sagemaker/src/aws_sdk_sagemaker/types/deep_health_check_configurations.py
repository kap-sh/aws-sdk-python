"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeepHealthCheckConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.instance_group_health_check_configuration

DeepHealthCheckConfigurations: TypeAlias = list[
    "aws_sdk_sagemaker.types.instance_group_health_check_configuration.InstanceGroupHealthCheckConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeepHealthCheckConfigurations) -> list:
    import aws_sdk_sagemaker.types.instance_group_health_check_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.instance_group_health_check_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DeepHealthCheckConfigurations:
    import aws_sdk_sagemaker.types.instance_group_health_check_configuration

    out: DeepHealthCheckConfigurations = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.instance_group_health_check_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
