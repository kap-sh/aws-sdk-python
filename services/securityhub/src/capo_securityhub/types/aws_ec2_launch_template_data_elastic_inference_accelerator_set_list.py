"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_details

AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetList: TypeAlias = list[
    "capo_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_details.AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetList,
) -> list:
    import capo_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetList:
    import capo_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_details

    out: AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_ec2_launch_template_data_elastic_inference_accelerator_set_details.deserialize_json(
                item
            )
        )
    return out
