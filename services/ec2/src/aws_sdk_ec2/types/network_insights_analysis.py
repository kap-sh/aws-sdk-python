"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInsightsAnalysis``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.alternate_path_hint_list
    import aws_sdk_ec2.types.analysis_status
    import aws_sdk_ec2.types.arn_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.explanation_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.network_insights_analysis_id
    import aws_sdk_ec2.types.network_insights_path_id
    import aws_sdk_ec2.types.path_component_list
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.value_string_list


class NetworkInsightsAnalysis(TypedDict):
    network_insights_analysis_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_analysis_id.NetworkInsightsAnalysisId"
    ]
    """<p>The ID of the network insights analysis.</p>"""
    network_insights_analysis_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the network insights analysis.</p>"""
    network_insights_path_id: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id.NetworkInsightsPathId"
    ]
    """<p>The ID of the path.</p>"""
    additional_accounts: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The member accounts that contain resources that the path can traverse.</p>"""
    filter_in_arns: NotRequired["aws_sdk_ec2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARN) of the resources that the path must traverse.</p>"""
    filter_out_arns: NotRequired["aws_sdk_ec2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARN) of the resources that the path must ignore.</p>"""
    start_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time the analysis started.</p>"""
    status: NotRequired["aws_sdk_ec2.types.analysis_status.AnalysisStatus"]
    """<p>The status of the network insights analysis.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message, if the status is <code>failed</code>.</p>"""
    warning_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The warning message.</p>"""
    network_path_found: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the destination is reachable from the source.</p>"""
    forward_path_components: NotRequired[
        "aws_sdk_ec2.types.path_component_list.PathComponentList"
    ]
    """<p>The components in the path from source to destination.</p>"""
    return_path_components: NotRequired[
        "aws_sdk_ec2.types.path_component_list.PathComponentList"
    ]
    """<p>The components in the path from destination to source.</p>"""
    explanations: NotRequired["aws_sdk_ec2.types.explanation_list.ExplanationList"]
    """<p>The explanations. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html\">Reachability Analyzer explanation codes</a>.</p>"""
    alternate_path_hints: NotRequired[
        "aws_sdk_ec2.types.alternate_path_hint_list.AlternatePathHintList"
    ]
    """<p>Potential intermediate components.</p>"""
    suggested_accounts: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>Potential intermediate accounts.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
