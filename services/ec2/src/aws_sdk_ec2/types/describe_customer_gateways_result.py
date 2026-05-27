"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCustomerGatewaysResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.customer_gateway_list


class DescribeCustomerGatewaysResult(TypedDict):
    customer_gateways: NotRequired[
        "aws_sdk_ec2.types.customer_gateway_list.CustomerGatewayList"
    ]
    """<p>Information about one or more customer gateways.</p>"""
