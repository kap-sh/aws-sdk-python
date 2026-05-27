"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamAddressHistoryResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_address_history_record_set
    import aws_sdk_ec2.types.next_token


class GetIpamAddressHistoryResult(TypedDict):
    history_records: NotRequired[
        "aws_sdk_ec2.types.ipam_address_history_record_set.IpamAddressHistoryRecordSet"
    ]
    """<p>A historical record for a CIDR within an IPAM scope. If the CIDR is associated with an EC2 instance, you will see an object in the response for the instance and one for the network interface.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
