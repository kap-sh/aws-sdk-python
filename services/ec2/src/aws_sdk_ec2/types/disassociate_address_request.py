"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.eip_allocation_public_ip
    import aws_sdk_ec2.types.elastic_ip_association_id


class DisassociateAddressRequest(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.elastic_ip_association_id.ElasticIpAssociationId"
    ]
    """<p>The association ID. This parameter is required.</p>"""
    public_ip: NotRequired[
        "aws_sdk_ec2.types.eip_allocation_public_ip.EipAllocationPublicIp"
    ]
    """<p>Deprecated.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
