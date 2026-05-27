"""Generated from Smithy shape ``com.amazonaws.ecs#ListTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.desired_status
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.string


class ListTasksRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListTasks</code> results. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container_instance: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container instance ID or full ARN of the container instance to use when filtering the <code>ListTasks</code> results. Specifying a <code>containerInstance</code> limits the results to tasks that belong to that container instance.</p>"""
    family: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the task definition family to use when filtering the <code>ListTasks</code> results. Specifying a <code>family</code> limits the results to tasks that belong to that family.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListTasks</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of task results that <code>ListTasks</code> returned in paginated output. When this parameter is used, <code>ListTasks</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTasks</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTasks</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    started_by: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>startedBy</code> value to filter the task results with. Specifying a <code>startedBy</code> value limits the results to tasks that were started with that value.</p> <p>When you specify <code>startedBy</code> as the filter, it must be the only filter that you use.</p>"""
    service_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the service to use when filtering the <code>ListTasks</code> results. Specifying a <code>serviceName</code> limits the results to tasks that belong to that service.</p>"""
    desired_status: NotRequired["aws_sdk_ecs.types.desired_status.DesiredStatus"]
    """<p>The task desired status to use when filtering the <code>ListTasks</code> results. Specifying a <code>desiredStatus</code> of <code>STOPPED</code> limits the results to tasks that Amazon ECS has set the desired status to <code>STOPPED</code>. This can be useful for debugging tasks that aren't starting properly or have died or finished. The default status filter is <code>RUNNING</code>, which shows tasks that Amazon ECS has set the desired status to <code>RUNNING</code>.</p> <note> <p>Although you can filter results based on a desired status of <code>PENDING</code>, this doesn't return any results. Amazon ECS never sets the desired status of a task to that value (only a task's <code>lastStatus</code> may have a value of <code>PENDING</code>).</p> </note>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The launch type to use when filtering the <code>ListTasks</code> results.</p>"""
    daemon_name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the daemon to use when filtering the <code>ListTasks</code> results. Specifying a <code>daemonName</code> limits the results to tasks that belong to that daemon.</p>"""
