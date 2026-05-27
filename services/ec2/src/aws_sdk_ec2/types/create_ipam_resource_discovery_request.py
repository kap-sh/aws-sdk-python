"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamResourceDiscoveryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_operating_region_set
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateIpamResourceDiscoveryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the IPAM resource discovery.</p>"""
    operating_regions: NotRequired[
        "aws_sdk_ec2.types.add_ipam_operating_region_set.AddIpamOperatingRegionSet"
    ]
    """<p>Operating Regions for the IPAM resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Tag specifications for the IPAM resource discovery.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A client token for the IPAM resource discovery.</p>"""
