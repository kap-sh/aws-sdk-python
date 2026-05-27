"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAccessScopeAnalysis``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_status
    import aws_sdk_ec2.types.findings_found
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_access_scope_analysis_id
    import aws_sdk_ec2.types.network_insights_access_scope_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NetworkInsightsAccessScopeAnalysis(TypedDict):
    network_insights_access_scope_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_analysis_id.NetworkInsightsAccessScopeAnalysisId"
    ]
    """<p>The ID of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_analysis_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Network Access Scope analysis.</p>"""
    network_insights_access_scope_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_access_scope_id.NetworkInsightsAccessScopeId"
    ]
    """<p>The ID of the Network Access Scope.</p>"""
    status: NotRequired["aws_sdk_ec2.types.analysis_status.AnalysisStatus"]
    """<p>The status.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message.</p>"""
    warning_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The warning message.</p>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The analysis start date.</p>"""
    end_date: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The analysis end date.</p>"""
    findings_found: NotRequired["aws_sdk_ec2.types.findings_found.FindingsFound"]
    """<p>Indicates whether there are findings.</p>"""
    analyzed_eni_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of network interfaces analyzed.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
