"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPlacementScores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_placement_score

SpotPlacementScores: TypeAlias = list[
    "aws_sdk_ec2.types.spot_placement_score.SpotPlacementScore"
]
