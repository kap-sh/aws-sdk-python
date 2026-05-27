"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_list
    import aws_sdk_ecs.types.failures


class DescribeDaemonDeploymentsResponse(TypedDict):
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
    daemon_deployments: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_list.DaemonDeploymentList"
    ]
    """<p>The list of daemon deployments.</p>"""
