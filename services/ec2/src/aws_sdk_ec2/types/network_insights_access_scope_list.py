"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope

NetworkInsightsAccessScopeList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_access_scope.NetworkInsightsAccessScope"
]
