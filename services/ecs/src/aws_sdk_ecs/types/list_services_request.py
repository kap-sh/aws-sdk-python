"""Generated from Smithy shape ``com.amazonaws.ecs#ListServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.launch_type
    import aws_sdk_ecs.types.resource_management_type
    import aws_sdk_ecs.types.scheduling_strategy
    import aws_sdk_ecs.types.string


class ListServicesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to use when filtering the <code>ListServices</code> results. If you do not specify a cluster, the default cluster is assumed.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListServices</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of service results that <code>ListServices</code> returned in paginated output. When this parameter is used, <code>ListServices</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServices</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServices</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>"""
    launch_type: NotRequired["aws_sdk_ecs.types.launch_type.LaunchType"]
    """<p>The launch type to use when filtering the <code>ListServices</code> results.</p>"""
    scheduling_strategy: NotRequired[
        "aws_sdk_ecs.types.scheduling_strategy.SchedulingStrategy"
    ]
    """<p>The scheduling strategy to use when filtering the <code>ListServices</code> results.</p>"""
    resource_management_type: NotRequired[
        "aws_sdk_ecs.types.resource_management_type.ResourceManagementType"
    ]
    """<p>The resourceManagementType type to use when filtering the <code>ListServices</code> results.</p>"""
