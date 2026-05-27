"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeContent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_path_list
    import aws_sdk_ec2.types.network_insights_access_scope_id


class NetworkInsightsAccessScopeContent(TypedDict):
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    match_paths: NotRequired[
        "aws_sdk_ec2.types.access_scope_path_list.AccessScopePathList"
    ]
    """<p>The paths to match.</p>"""
    exclude_paths: NotRequired[
        "aws_sdk_ec2.types.access_scope_path_list.AccessScopePathList"
    ]
    """<p>The paths to exclude.</p>"""
