"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_summaries_list
    import aws_sdk_ecs.types.string


class ListDaemonsResponse(TypedDict):
    daemon_summaries_list: NotRequired[
        "aws_sdk_ecs.types.daemon_summaries_list.DaemonSummariesList"
    ]
    """<p>The list of daemon summaries.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListDaemons</code> request. When the results of a <code>ListDaemons</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results.</p>"""
