"""Generated from Smithy shape ``com.amazonaws.ec2#GetAwsNetworkPerformanceDataResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.data_responses
    import aws_sdk_ec2.types.string


class GetAwsNetworkPerformanceDataResult(TypedDict):
    data_responses: NotRequired["aws_sdk_ec2.types.data_responses.DataResponses"]
    """<p>The list of data responses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
