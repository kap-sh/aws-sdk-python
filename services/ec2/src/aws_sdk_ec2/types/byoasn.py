"""Generated from Smithy shape ``com.amazonaws.ec2#Byoasn``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_state
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.string


class Byoasn(TypedDict):
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A public 2-byte or 4-byte ASN.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>An IPAM ID.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message.</p>"""
    state: NotRequired["aws_sdk_ec2.types.asn_state.AsnState"]
    """<p>The provisioning state of the BYOASN.</p>"""
