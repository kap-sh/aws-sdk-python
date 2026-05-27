"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplatesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_launch_templates_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.launch_template_id_string_list
    import aws_sdk_ec2.types.launch_template_name_string_list
    import aws_sdk_ec2.types.string


class DescribeLaunchTemplatesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    launch_template_ids: NotRequired[
        "aws_sdk_ec2.types.launch_template_id_string_list.LaunchTemplateIdStringList"
    ]
    """<p>One or more launch template IDs.</p>"""
    launch_template_names: NotRequired[
        "aws_sdk_ec2.types.launch_template_name_string_list.LaunchTemplateNameStringList"
    ]
    """<p>One or more launch template names.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>create-time</code> - The time the launch template was created.</p> </li> <li> <p> <code>launch-template-name</code> - The name of the launch template.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to request the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_launch_templates_max_results.DescribeLaunchTemplatesMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value. This value can be between 1 and 200.</p>"""
    include_managed_resources: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include managed resources in the output. If this parameter is set to <code>true</code>, the output includes resources that are managed by Amazon Web Services services, even if managed resource visibility is set to hidden.</p>"""
