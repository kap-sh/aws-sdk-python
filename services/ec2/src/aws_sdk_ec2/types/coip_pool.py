"""Generated from Smithy shape ``com.amazonaws.ec2#CoipPool``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_coip_id
    import aws_sdk_ec2.types.local_gateway_routetable_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class CoipPool(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_coip_id.Ipv4PoolCoipId"]
    """<p>The ID of the address pool.</p>"""
    pool_cidrs: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The address ranges of the address pool.</p>"""
    local_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_routetable_id.LocalGatewayRoutetableId"
    ]
    """<p>The ID of the local gateway route table.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    pool_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the address pool.</p>"""
