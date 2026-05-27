"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeCapacityProvidersResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_providers
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.string


class DescribeCapacityProvidersResponse(TypedDict):
    capacity_providers: NotRequired[
        "aws_sdk_ecs.types.capacity_providers.CapacityProviders"
    ]
    """<p>The list of capacity providers.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeCapacityProviders</code> request. When the results of a <code>DescribeCapacityProviders</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
