"""Generated from Smithy shape ``com.amazonaws.ecs#ListContainerInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.container_instance_status
    import aws_sdk_ecs.types.string


class ListContainerInstancesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.</p>"""
    filter: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html\">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListContainerInstances</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of container instance results that <code>ListContainerInstances</code> returned in paginated output. When this parameter is used, <code>ListContainerInstances</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListContainerInstances</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListContainerInstances</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.container_instance_status.ContainerInstanceStatus"
    ]
    """<p>Filters the container instances by status. For example, if you specify the <code>DRAINING</code> status, the results include only container instances that have been set to <code>DRAINING</code> using <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html\">UpdateContainerInstancesState</a>. If you don't specify this parameter, the The default is to include container instances set to all states other than <code>INACTIVE</code>.</p>"""
