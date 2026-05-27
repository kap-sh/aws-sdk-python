"""Generated from Smithy shape ``com.amazonaws.ecs#ListTasksResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListTasksResponse(TypedDict):
    task_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of task ARN entries for the <code>ListTasks</code> request.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListTasks</code> request. When the results of a <code>ListTasks</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
