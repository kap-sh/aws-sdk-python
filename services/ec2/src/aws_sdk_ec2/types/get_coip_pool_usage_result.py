"""Generated from Smithy shape ``com.amazonaws.ec2#GetCoipPoolUsageResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_address_usage_set
    import aws_sdk_ec2.types.string


class GetCoipPoolUsageResult(TypedDict):
    coip_pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the customer-owned address pool.</p>"""
    coip_address_usages: NotRequired[
        "aws_sdk_ec2.types.coip_address_usage_set.CoipAddressUsageSet"
    ]
    """<p>Information about the address usage.</p>"""
    local_gateway_route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the local gateway route table.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
