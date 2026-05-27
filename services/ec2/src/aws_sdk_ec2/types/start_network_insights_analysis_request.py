"""Generated from Smithy shape ``com.amazonaws.ec2#StartNetworkInsightsAnalysisRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.arn_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_insights_path_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.value_string_list


class StartNetworkInsightsAnalysisRequest(TypedDict):
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
    """<p>The Amazon Resource Names (ARN) of the resources that the path will ignore.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
