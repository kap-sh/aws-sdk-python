"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceDeploymentsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.service_deployments


class DescribeServiceDeploymentsResponse(TypedDict):
    service_deployments: NotRequired[
        "aws_sdk_ecs.types.service_deployments.ServiceDeployments"
    ]
    """<p>The list of service deployments described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p> <p>If you decsribe a deployment with a service revision created before October 25, 2024, the call fails. The failure includes the service revision ARN and the reason set to <code>MISSING</code>.</p>"""
