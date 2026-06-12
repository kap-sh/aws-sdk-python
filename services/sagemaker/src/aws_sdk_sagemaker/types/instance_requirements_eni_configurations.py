"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceRequirementsEniConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.instance_requirements_eni_configuration

InstanceRequirementsEniConfigurations: TypeAlias = list[
    "aws_sdk_sagemaker.types.instance_requirements_eni_configuration.InstanceRequirementsEniConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceRequirementsEniConfigurations) -> list:
    import aws_sdk_sagemaker.types.instance_requirements_eni_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.instance_requirements_eni_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceRequirementsEniConfigurations:
    import aws_sdk_sagemaker.types.instance_requirements_eni_configuration

    out: InstanceRequirementsEniConfigurations = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.instance_requirements_eni_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
