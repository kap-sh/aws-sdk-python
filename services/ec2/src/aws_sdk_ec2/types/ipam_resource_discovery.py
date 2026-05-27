"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscovery``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_operating_region_set
    import aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.ipam_resource_discovery_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamResourceDiscovery(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the owner.</p>"""
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The resource discovery ID.</p>"""
    ipam_resource_discovery_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource discovery Amazon Resource Name (ARN).</p>"""
    ipam_resource_discovery_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource discovery Region.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource discovery description.</p>"""
    operating_regions: NotRequired[
        "aws_sdk_ec2.types.ipam_operating_region_set.IpamOperatingRegionSet"
    ]
    """<p>The operating Regions for the resource discovery. Operating Regions are Amazon Web Services Regions where the IPAM is allowed to manage IP address CIDRs. IPAM only discovers and monitors resources in the Amazon Web Services Regions you select as operating Regions.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if the resource discovery is the default. The default resource discovery is the resource discovery automatically created when you create an IPAM.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_state.IpamResourceDiscoveryState"
    ]
    """<p>The lifecycle state of the resource discovery.</p> <ul> <li> <p> <code>create-in-progress</code> - Resource discovery is being created.</p> </li> <li> <p> <code>create-complete</code> - Resource discovery creation is complete.</p> </li> <li> <p> <code>create-failed</code> - Resource discovery creation has failed.</p> </li> <li> <p> <code>modify-in-progress</code> - Resource discovery is being modified.</p> </li> <li> <p> <code>modify-complete</code> - Resource discovery modification is complete.</p> </li> <li> <p> <code>modify-failed</code> - Resource discovery modification has failed.</p> </li> <li> <p> <code>delete-in-progress</code> - Resource discovery is being deleted.</p> </li> <li> <p> <code>delete-complete</code> - Resource discovery deletion is complete.</p> </li> <li> <p> <code>delete-failed</code> - Resource discovery deletion has failed.</p> </li> <li> <p> <code>isolate-in-progress</code> - Amazon Web Services account that created the resource discovery has been removed and the resource discovery is being isolated.</p> </li> <li> <p> <code>isolate-complete</code> - Resource discovery isolation is complete.</p> </li> <li> <p> <code>restore-in-progress</code> - Amazon Web Services account that created the resource discovery and was isolated has been restored.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""
    organizational_unit_exclusions: NotRequired[
        "aws_sdk_ec2.types.ipam_organizational_unit_exclusion_set.IpamOrganizationalUnitExclusionSet"
    ]
    """<p>If your IPAM is integrated with Amazon Web Services Organizations and you add an organizational unit (OU) exclusion, IPAM will not manage the IP addresses in accounts in that OU exclusion.</p>"""
