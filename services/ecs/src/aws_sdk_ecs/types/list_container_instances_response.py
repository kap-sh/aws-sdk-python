"""Generated from Smithy shape ``com.amazonaws.ecs#ListContainerInstancesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListContainerInstancesResponse(TypedDict):
    container_instance_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of container instances with full ARN entries for each container instance associated with the specified cluster.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListContainerInstances</code> request. When the results of a <code>ListContainerInstances</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
