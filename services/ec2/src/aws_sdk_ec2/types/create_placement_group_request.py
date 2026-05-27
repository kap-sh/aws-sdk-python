"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePlacementGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.operator_request
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_strategy
    import aws_sdk_ec2.types.spread_level
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreatePlacementGroupRequest(TypedDict):
    partition_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of partitions. Valid only when <b>Strategy</b> is set to <code>partition</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new placement group.</p>"""
    spread_level: NotRequired["aws_sdk_ec2.types.spread_level.SpreadLevel"]
    """<p>Determines how placement groups spread instances. </p> <ul> <li> <p>Host – You can use <code>host</code> only with Outpost placement groups.</p> </li> <li> <p>Rack – No usage restrictions.</p> </li> </ul>"""
    linked_group_id: NotRequired[
        "aws_sdk_ec2.types.placement_group_id.PlacementGroupId"
    ]
    """<p>Reserved for future use.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the placement group. Must be unique within the scope of your account for the Region.</p> <p>Constraints: Up to 255 ASCII characters</p>"""
    strategy: NotRequired["aws_sdk_ec2.types.placement_strategy.PlacementStrategy"]
    """<p>The placement strategy.</p>"""
