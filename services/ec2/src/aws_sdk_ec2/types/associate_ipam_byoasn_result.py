"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIpamByoasnResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_association


class AssociateIpamByoasnResult(TypedDict):
    asn_association: NotRequired["aws_sdk_ec2.types.asn_association.AsnAssociation"]
    """<p>The ASN and BYOIP CIDR association.</p>"""
