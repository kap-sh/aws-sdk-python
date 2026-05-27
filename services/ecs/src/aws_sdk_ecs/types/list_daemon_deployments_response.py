"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_summary_list
    import aws_sdk_ecs.types.string


class ListDaemonDeploymentsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListDaemonDeployments</code> request. When the results of a <code>ListDaemonDeployments</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results.</p>"""
    daemon_deployments: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_summary_list.DaemonDeploymentSummaryList"
    ]
    """<p>The list of daemon deployment summaries.</p>"""
