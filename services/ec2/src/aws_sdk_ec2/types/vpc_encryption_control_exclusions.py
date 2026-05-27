"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControlExclusions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_encryption_control_exclusion

VpcEncryptionControlExclusions = TypedDict(
    "VpcEncryptionControlExclusions",
    {
        "internet_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "egress_only_internet_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "nat_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "virtual_private_gateway": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "vpc_peering": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "lambda": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "vpc_lattice": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
        "elastic_file_system": NotRequired[
            "aws_sdk_ec2.types.vpc_encryption_control_exclusion.VpcEncryptionControlExclusion"
        ],
    },
)
