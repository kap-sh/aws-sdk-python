"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInsightsAccessScopeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_path_list_request
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateNetworkInsightsAccessScopeRequest(TypedDict):
    match_paths: NotRequired[
        "aws_sdk_ec2.types.access_scope_path_list_request.AccessScopePathListRequest"
    ]
    """<p>The paths to match.</p>"""
    exclude_paths: NotRequired[
        "aws_sdk_ec2.types.access_scope_path_list_request.AccessScopePathListRequest"
    ]
    """<p>The paths to exclude.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">How to ensure idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
