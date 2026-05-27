"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonTaskDefinitionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.daemon_task_definition_revision_filter
    import aws_sdk_ecs.types.daemon_task_definition_status_filter
    import aws_sdk_ecs.types.sort_order
    import aws_sdk_ecs.types.string


class ListDaemonTaskDefinitionsRequest(TypedDict):
    family_prefix: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The full family name to filter the <code>ListDaemonTaskDefinitions</code> results with. Specifying a <code>familyPrefix</code> limits the listed daemon task definitions to daemon task definition families that start with the <code>familyPrefix</code> string.</p>"""
    family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The exact name of the daemon task definition family to filter results with.</p>"""
    revision: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition_revision_filter.DaemonTaskDefinitionRevisionFilter"
    ]
    """<p>The revision filter to apply. Specify <code>LAST_REGISTERED</code> to return only the last registered revision for each daemon task definition family.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_task_definition_status_filter.DaemonTaskDefinitionStatusFilter"
    ]
    """<p>The daemon task definition status to filter the <code>ListDaemonTaskDefinitions</code> results with. By default, only <code>ACTIVE</code> daemon task definitions are listed. If you set this parameter to <code>DELETE_IN_PROGRESS</code>, only daemon task definitions that are in the process of being deleted are listed. If you set this parameter to <code>ALL</code>, all daemon task definitions are listed regardless of status.</p>"""
    sort: NotRequired["aws_sdk_ecs.types.sort_order.SortOrder"]
    """<p>The order to sort the results. Valid values are <code>ASC</code> and <code>DESC</code>. By default (<code>ASC</code>), daemon task definitions are listed in ascending order by family name and revision number.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListDaemonTaskDefinitions</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of daemon task definition results that <code>ListDaemonTaskDefinitions</code> returned in paginated output. When this parameter is used, <code>ListDaemonTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonTaskDefinitions</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonTaskDefinitions</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
