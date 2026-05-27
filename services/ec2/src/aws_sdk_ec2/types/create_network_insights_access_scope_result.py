"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsAccessScopeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope
    import aws_sdk_ec2.types.network_insights_access_scope_content


class CreateNetworkInsightsAccessScopeResult(TypedDict):
    network_insights_access_scope: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope.NetworkInsightsAccessScope"
    ]
    """<p>The Network Access Scope.</p>"""
    network_insights_access_scope_content: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_content.NetworkInsightsAccessScopeContent"
    ]
    """<p>The Network Access Scope content.</p>"""
