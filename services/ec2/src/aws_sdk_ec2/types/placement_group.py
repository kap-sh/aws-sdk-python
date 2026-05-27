"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.operator_response
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_group_state
    import aws_sdk_ec2.types.placement_strategy
    import aws_sdk_ec2.types.spread_level
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class PlacementGroup(TypedDict):
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the placement group.</p>"""
    state: NotRequired["aws_sdk_ec2.types.placement_group_state.PlacementGroupState"]
    """<p>The state of the placement group.</p>"""
    strategy: NotRequired["aws_sdk_ec2.types.placement_strategy.PlacementStrategy"]
    """<p>The placement strategy.</p>"""
    partition_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of partitions. Valid only if <b>strategy</b> is set to <code>partition</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the placement group.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the placement group.</p>"""
    group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the placement group.</p>"""
    spread_level: NotRequired["aws_sdk_ec2.types.spread_level.SpreadLevel"]
    """<p>The spread level for the placement group. <i>Only</i> Outpost placement groups can be spread across hosts.</p>"""
    linked_group_id: NotRequired[
        "aws_sdk_ec2.types.placement_group_id.PlacementGroupId"
    ]
    """<p>Reserved for future use.</p>"""
    operator: NotRequired["aws_sdk_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the Placement Group.</p>"""
