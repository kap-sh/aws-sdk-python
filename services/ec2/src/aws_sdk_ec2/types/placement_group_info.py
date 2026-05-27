"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroupInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_strategy_list


class PlacementGroupInfo(TypedDict):
    supported_strategies: NotRequired[
        "aws_sdk_ec2.types.placement_group_strategy_list.PlacementGroupStrategyList"
    ]
    """<p>The supported placement group types.</p>"""
