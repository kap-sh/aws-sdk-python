"""Generated from Smithy shape ``com.amazonaws.ecs#ListServicesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListServicesResponse(TypedDict):
    service_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of full ARN entries for each service that's associated with the specified cluster.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListServices</code> request. When the results of a <code>ListServices</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
