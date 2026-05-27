"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonTaskDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_task_definition_summaries
    import aws_sdk_ecs.types.string


class ListDaemonTaskDefinitionsResponse(TypedDict):
    daemon_task_definitions: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition_summaries.DaemonTaskDefinitionSummaries"
    ]
    """<p>The list of daemon task definition summaries.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListDaemonTaskDefinitions</code> request. When the results of a <code>ListDaemonTaskDefinitions</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results.</p>"""
