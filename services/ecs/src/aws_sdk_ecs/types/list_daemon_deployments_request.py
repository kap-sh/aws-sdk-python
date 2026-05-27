"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonDeploymentsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.created_at
    import aws_sdk_ecs.types.daemon_deployment_status_list
    import aws_sdk_ecs.types.string


class ListDaemonDeploymentsRequest(TypedDict):
    daemon_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to list deployments for.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_status_list.DaemonDeploymentStatusList"
    ]
    """<p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by deployment status. If you don't specify a status, all deployments are returned.</p>"""
    created_at: NotRequired["aws_sdk_ecs.types.created_at.CreatedAt"]
    """<p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by creation time. If you don't specify a time range, all deployments are returned.</p>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of daemon deployment results that <code>ListDaemonDeployments</code> returned in paginated output. When this parameter is used, <code>ListDaemonDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListDaemonDeployments</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
