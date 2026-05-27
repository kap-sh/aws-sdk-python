"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceDiscoveryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_operating_region_set
    import aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.remove_ipam_operating_region_set
    import aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.string


class ModifyIpamResourceDiscoveryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>A resource discovery ID.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A resource discovery description.</p>"""
    add_operating_regions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
    ]
    """<p>Add operating Regions to the resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p>"""
    remove_operating_regions: NotRequired[
        "aws_sdk_ec2.types.remove_ipam_operating_region_set.RemoveIpamOperatingRegionSet"
    ]
    """<p>Remove operating Regions.</p>"""
    add_organizational_unit_exclusions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_organizational_unit_exclusion_set.AddIpamOrganizationalUnitExclusionSet"
    ]
    """<p>Add an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html\">Quotas for your IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <note> <p>The resulting set of exclusions must not result in \"overlap\", meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the Amazon Web Services CLI request process in <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete\">Add or remove OU exclusions </a> in the <i>Amazon VPC User Guide</i>.</p> </note>"""
    remove_organizational_unit_exclusions: NotRequired[
        "aws_sdk_ec2.types.remove_ipam_organizational_unit_exclusion_set.RemoveIpamOrganizationalUnitExclusionSet"
    ]
    """<p>Remove an Organizational Unit (OU) exclusion to your IPAM. If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion. There is a limit on the number of exclusions you can create. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html\">Quotas for your IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p> <note> <p>The resulting set of exclusions must not result in \"overlap\", meaning two or more OU exclusions must not exclude the same OU. For more information and examples, see the Amazon Web Services CLI request process in <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/exclude-ous.html#exclude-ous-create-delete\">Add or remove OU exclusions </a> in the <i>Amazon VPC User Guide</i>.</p> </note>"""
