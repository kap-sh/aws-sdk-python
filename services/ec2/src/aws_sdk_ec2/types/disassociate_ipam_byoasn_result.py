"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIpamByoasnResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_association


class DisassociateIpamByoasnResult(TypedDict):
    asn_association: NotRequired["aws_sdk_ec2.types.asn_association.AsnAssociation"]
    """<p>An ASN and BYOIP CIDR association.</p>"""
