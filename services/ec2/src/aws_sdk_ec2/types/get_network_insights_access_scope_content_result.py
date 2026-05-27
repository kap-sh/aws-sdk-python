"""Generated from Smithy shape ``com.amazonaws.ec2#GetNetworkInsightsAccessScopeContentResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_content


class GetNetworkInsightsAccessScopeContentResult(TypedDict):
    network_insights_access_scope_content: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_content.NetworkInsightsAccessScopeContent"
    ]
    """<p>The Network Access Scope content.</p>"""
