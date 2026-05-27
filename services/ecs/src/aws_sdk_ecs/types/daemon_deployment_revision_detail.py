"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentRevisionDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.daemon_deployment_capacity_provider_list
    import aws_sdk_ecs.types.string


class DaemonDeploymentRevisionDetail(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the daemon revision.</p>"""
    capacity_providers: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_capacity_provider_list.DaemonDeploymentCapacityProviderList"
    ]
    """<p>The capacity providers associated with this daemon revision during the deployment.</p>"""
    total_running_instance_count: NotRequired[
        "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The total number of instances running daemon tasks for this revision.</p>"""
    total_draining_instance_count: NotRequired[
        "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The total number of instances being drained for this revision during the deployment.</p>"""
