"""Generated from Smithy shape ``com.amazonaws.ec2#AsnAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.asn_association_state
    import aws_sdk_ec2.types.string


class AsnAssociation(TypedDict):
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association's ASN.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association's CIDR.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association's status message.</p>"""
    state: NotRequired["aws_sdk_ec2.types.asn_association_state.AsnAssociationState"]
    """<p>The association's state.</p>"""
