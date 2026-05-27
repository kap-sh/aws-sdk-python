"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopeAnalysisFinding``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.path_component_list
    import aws_sdk_ec2.types.string


class AccessScopeAnalysisFinding(TypedDict):
    network_insights_access_scope_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    finding_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the finding.</p>"""
    finding_components: NotRequired[
        "aws_sdk_ec2.types.path_component_list.PathComponentList"
    ]
    """<p>The finding components.</p>"""
