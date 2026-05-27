"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamByoasnResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.byoasn_set
    import aws_sdk_ec2.types.string


class DescribeIpamByoasnResult(TypedDict):
    byoasns: NotRequired["aws_sdk_ec2.types.byoasn_set.ByoasnSet"]
    """<p>ASN and BYOIP CIDR associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
