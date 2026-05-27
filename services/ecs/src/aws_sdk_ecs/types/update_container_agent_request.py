"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerAgentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class UpdateContainerAgentRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container_instance: "aws_sdk_ecs.types.string.String"
    """<p>The container instance ID or full ARN entries for the container instance where you would like to update the Amazon ECS container agent.</p>"""
