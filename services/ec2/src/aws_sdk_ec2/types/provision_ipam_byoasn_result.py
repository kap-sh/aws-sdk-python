"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionIpamByoasnResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.byoasn


class ProvisionIpamByoasnResult(TypedDict):
    byoasn: NotRequired["aws_sdk_ec2.types.byoasn.Byoasn"]
    """<p>An ASN and BYOIP CIDR association.</p>"""
