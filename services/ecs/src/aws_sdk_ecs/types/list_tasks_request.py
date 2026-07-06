"""Generated from Smithy shape ``com.amazonaws.ecs#ListTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.desired_status
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.string


class ListTasksRequest(TypedDict, closed=True):
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTasksRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "container_instance" in value:
        out["containerInstance"] = value["container_instance"]
    if "family" in value:
        out["family"] = value["family"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "desired_status" in value:
        import aws_sdk_ecs.types.desired_status

        out["desiredStatus"] = aws_sdk_ecs.types.desired_status.serialize_aws_json_1_1(
            value["desired_status"]
        )
    if "launch_type" in value:
        import aws_sdk_ecs.types.launch_type

        out["launchType"] = aws_sdk_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "daemon_name" in value:
        out["daemonName"] = value["daemon_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTasksRequest:
    out: ListTasksRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "containerInstance" in data:
        out["container_instance"] = data["containerInstance"]
    if "family" in data:
        out["family"] = data["family"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "startedBy" in data:
        out["started_by"] = data["startedBy"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "desiredStatus" in data:
        import aws_sdk_ecs.types.desired_status

        out["desired_status"] = (
            aws_sdk_ecs.types.desired_status.deserialize_aws_json_1_1(
                data["desiredStatus"]
            )
        )
    if "launchType" in data:
        import aws_sdk_ecs.types.launch_type

        out["launch_type"] = aws_sdk_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if "daemonName" in data:
        out["daemon_name"] = data["daemonName"]
    return out
