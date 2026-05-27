"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsPathIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_path_id

NetworkInsightsPathIdList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
]
