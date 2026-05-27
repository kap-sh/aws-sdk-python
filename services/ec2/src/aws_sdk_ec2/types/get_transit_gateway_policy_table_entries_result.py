"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPolicyTableEntriesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_policy_table_entry_list


class GetTransitGatewayPolicyTableEntriesResult(TypedDict):
    transit_gateway_policy_table_entries: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_entry_list.TransitGatewayPolicyTableEntryList"
    ]
    """<p>The entries for the transit gateway policy table.</p>"""
