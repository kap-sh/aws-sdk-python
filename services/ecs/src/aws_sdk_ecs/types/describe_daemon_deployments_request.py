"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonDeploymentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class DescribeDaemonDeploymentsRequest(TypedDict):
    daemon_deployment_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The ARN of the daemon deployments to describe. You can specify up to 20 ARNs.</p>"""
