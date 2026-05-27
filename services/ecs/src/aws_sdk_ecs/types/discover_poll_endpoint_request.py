"""Generated from Smithy shape ``com.amazonaws.ecs#DiscoverPollEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DiscoverPollEndpointRequest(TypedDict):
    container_instance: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The container instance ID or full ARN of the container instance. For more information about the ARN format, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids\">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that the container instance belongs to.</p>"""
