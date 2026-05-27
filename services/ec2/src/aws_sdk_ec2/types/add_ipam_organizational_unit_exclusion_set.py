"""Generated from Smithy shape ``com.amazonaws.ec2#AddIpamOrganizationalUnitExclusionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion

AddIpamOrganizationalUnitExclusionSet: TypeAlias = list[
    "aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion.AddIpamOrganizationalUnitExclusion"
]
