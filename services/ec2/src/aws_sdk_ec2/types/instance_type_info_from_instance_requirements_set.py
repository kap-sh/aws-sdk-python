"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeInfoFromInstanceRequirementsSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_info_from_instance_requirements

InstanceTypeInfoFromInstanceRequirementsSet: TypeAlias = list[
    "aws_sdk_ec2.types.instance_type_info_from_instance_requirements.InstanceTypeInfoFromInstanceRequirements"
]
