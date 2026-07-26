"""Generated from Smithy shape ``com.amazonaws.ecs#ListServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.launch_type
    import capo_ecs.types.resource_management_type
    import capo_ecs.types.scheduling_strategy
    import capo_ecs.types.string


class ListServicesRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListServices</code> results. If you do not specify a cluster, the default cluster is assumed.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListServices</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of service results that <code>ListServices</code> returned in paginated output. When this parameter is used, <code>ListServices</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServices</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServices</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>"""
    launch_type: NotRequired["capo_ecs.types.launch_type.LaunchType"]
    """<p>The launch type to use when filtering the <code>ListServices</code> results.</p>"""
    scheduling_strategy: NotRequired[
        "capo_ecs.types.scheduling_strategy.SchedulingStrategy"
    ]
    """<p>The scheduling strategy to use when filtering the <code>ListServices</code> results.</p>"""
    resource_management_type: NotRequired[
        "capo_ecs.types.resource_management_type.ResourceManagementType"
    ]
    """<p>The resourceManagementType type to use when filtering the <code>ListServices</code> results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServicesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "launch_type" in value:
        import capo_ecs.types.launch_type

        out["launchType"] = capo_ecs.types.launch_type.serialize_aws_json_1_1(
            value["launch_type"]
        )
    if "scheduling_strategy" in value:
        import capo_ecs.types.scheduling_strategy

        out["schedulingStrategy"] = (
            capo_ecs.types.scheduling_strategy.serialize_aws_json_1_1(
                value["scheduling_strategy"]
            )
        )
    if "resource_management_type" in value:
        import capo_ecs.types.resource_management_type

        out["resourceManagementType"] = (
            capo_ecs.types.resource_management_type.serialize_aws_json_1_1(
                value["resource_management_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServicesRequest:
    out: ListServicesRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "launchType" in data:
        import capo_ecs.types.launch_type

        out["launch_type"] = capo_ecs.types.launch_type.deserialize_aws_json_1_1(
            data["launchType"]
        )
    if "schedulingStrategy" in data:
        import capo_ecs.types.scheduling_strategy

        out["scheduling_strategy"] = (
            capo_ecs.types.scheduling_strategy.deserialize_aws_json_1_1(
                data["schedulingStrategy"]
            )
        )
    if "resourceManagementType" in data:
        import capo_ecs.types.resource_management_type

        out["resource_management_type"] = (
            capo_ecs.types.resource_management_type.deserialize_aws_json_1_1(
                data["resourceManagementType"]
            )
        )
    return out
