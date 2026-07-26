"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProvisioningParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.provisioning_parameter

ProvisioningParameters: TypeAlias = list[
    "capo_sagemaker.types.provisioning_parameter.ProvisioningParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningParameters) -> list:
    import capo_sagemaker.types.provisioning_parameter

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.provisioning_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningParameters:
    import capo_sagemaker.types.provisioning_parameter

    out: ProvisioningParameters = []
    for item in data:
        out.append(
            capo_sagemaker.types.provisioning_parameter.deserialize_aws_json_1_1(item)
        )
    return out
