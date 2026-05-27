"""Generated from Smithy shape ``com.amazonaws.ec2#GetVerifiedAccessEndpointTargetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_endpoint_target_list


class GetVerifiedAccessEndpointTargetsResult(TypedDict):
    verified_access_endpoint_targets: NotRequired[
        "aws_sdk_ec2.types.verified_access_endpoint_target_list.VerifiedAccessEndpointTargetList"
    ]
    """<p>The Verified Access targets.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
