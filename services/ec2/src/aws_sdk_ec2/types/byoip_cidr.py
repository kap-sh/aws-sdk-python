"""Generated from Smithy shape ``com.amazonaws.ec2#ByoipCidr``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_association_set
    import aws_sdk_ec2.types.byoip_cidr_state
    import aws_sdk_ec2.types.string


class ByoipCidr(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The address range, in CIDR notation.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the address range.</p>"""
    asn_associations: NotRequired[
        "aws_sdk_ec2.types.asn_association_set.AsnAssociationSet"
    ]
    """<p>The BYOIP CIDR associations with ASNs.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Upon success, contains the ID of the address pool. Otherwise, contains an error message.</p>"""
    state: NotRequired["aws_sdk_ec2.types.byoip_cidr_state.ByoipCidrState"]
    """<p>The state of the address range.</p> <ul> <li> <p> <code>advertised</code>: The address range is being advertised to the internet by Amazon Web Services.</p> </li> <li> <p> <code>deprovisioned</code>: The address range is deprovisioned.</p> </li> <li> <p> <code>failed-deprovision</code>: The request to deprovision the address range was unsuccessful. Ensure that all EIPs from the range have been deallocated and try again.</p> </li> <li> <p> <code>failed-provision</code>: The request to provision the address range was unsuccessful.</p> </li> <li> <p> <code>pending-deprovision</code>: You’ve submitted a request to deprovision an address range and it's pending.</p> </li> <li> <p> <code>pending-provision</code>: You’ve submitted a request to provision an address range and it's pending.</p> </li> <li> <p> <code>provisioned</code>: The address range is provisioned and can be advertised. The range is not currently advertised.</p> </li> <li> <p> <code>provisioned-not-publicly-advertisable</code>: The address range is provisioned and cannot be advertised.</p> </li> </ul>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If you have <a href=\"https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html\">Local Zones</a> enabled, you can choose a network border group for Local Zones when you provision and advertise a BYOIPv4 CIDR. Choose the network border group carefully as the EIP and the Amazon Web Services resource it is associated with must reside in the same network border group.</p> <p>You can provision BYOIP address ranges to and advertise them in the following Local Zone network border groups:</p> <ul> <li> <p>us-east-1-dfw-2</p> </li> <li> <p>us-west-2-lax-1</p> </li> <li> <p>us-west-2-phx-2</p> </li> </ul> <note> <p>You cannot provision or advertise BYOIPv6 address ranges in Local Zones at this time.</p> </note>"""
    advertisement_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies the advertisement method for the BYOIP CIDR. Valid values are:</p> <ul> <li> <p> <code>unicast</code>: IP is advertised from a single location (regional services like EC2)</p> </li> <li> <p> <code>anycast</code>: IP is advertised from multiple global locations simultaneously (global services like CloudFront)</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-cloudfront.html\">Bring your own IP to CloudFront using IPAM</a> in the <i>Amazon VPC IPAM User Guide</i>.</p>"""
