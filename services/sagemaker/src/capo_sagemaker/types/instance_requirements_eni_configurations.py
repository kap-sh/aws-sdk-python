"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceRequirementsEniConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.instance_requirements_eni_configuration

InstanceRequirementsEniConfigurations: TypeAlias = list[
    "capo_sagemaker.types.instance_requirements_eni_configuration.InstanceRequirementsEniConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceRequirementsEniConfigurations) -> list:
    import capo_sagemaker.types.instance_requirements_eni_configuration

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.instance_requirements_eni_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceRequirementsEniConfigurations:
    import capo_sagemaker.types.instance_requirements_eni_configuration

    out: InstanceRequirementsEniConfigurations = []
    for item in data:
        out.append(
            capo_sagemaker.types.instance_requirements_eni_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
