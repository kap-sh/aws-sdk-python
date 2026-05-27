"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIpamResourceDiscoveryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery_association


class AssociateIpamResourceDiscoveryResult(TypedDict):
    ipam_resource_discovery_association: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association.IpamResourceDiscoveryAssociation"
    ]
    """<p>A resource discovery association. An associated resource discovery is a resource discovery that has been associated with an IPAM.</p>"""
