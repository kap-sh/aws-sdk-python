"""Generated from Smithy shape ``com.amazonaws.ec2#RemoveIpamOrganizationalUnitExclusionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion

RemoveIpamOrganizationalUnitExclusionSet: TypeAlias = list[
    "aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion.RemoveIpamOrganizationalUnitExclusion"
]
