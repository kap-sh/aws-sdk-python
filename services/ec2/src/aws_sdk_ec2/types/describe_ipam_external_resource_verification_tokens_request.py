"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamExternalResourceVerificationTokensRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.ipam_max_results
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.value_string_list


class DescribeIpamExternalResourceVerificationTokensRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters for the request. For more information about filtering, see <a href=\"https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html\">Filtering CLI output</a>.</p> <p>Available filters:</p> <ul> <li> <p> <code>ipam-arn</code> </p> </li> <li> <p> <code>ipam-external-resource-verification-token-arn</code> </p> </li> <li> <p> <code>ipam-external-resource-verification-token-id</code> </p> </li> <li> <p> <code>ipam-id</code> </p> </li> <li> <p> <code>ipam-region</code> </p> </li> <li> <p> <code>state</code> </p> </li> <li> <p> <code>status</code> </p> </li> <li> <p> <code>token-name</code> </p> </li> <li> <p> <code>token-value</code> </p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of tokens to return in one page of results.</p>"""
    ipam_external_resource_verification_token_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>Verification token IDs.</p>"""
