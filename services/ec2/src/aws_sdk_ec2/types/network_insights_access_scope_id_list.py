"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_id

NetworkInsightsAccessScopeIdList: TypeAlias = list[
    "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
]
