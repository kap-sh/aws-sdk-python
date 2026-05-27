"""Generated from Smithy shape ``com.amazonaws.ec2#IpamOrganizationalUnitExclusionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_organizational_unit_exclusion

IpamOrganizationalUnitExclusionSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_organizational_unit_exclusion.IpamOrganizationalUnitExclusion"
]
