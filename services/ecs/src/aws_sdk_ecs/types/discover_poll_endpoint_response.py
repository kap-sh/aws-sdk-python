"""Generated from Smithy shape ``com.amazonaws.ecs#DiscoverPollEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DiscoverPollEndpointResponse(TypedDict):
    endpoint: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The endpoint for the Amazon ECS agent to poll.</p>"""
    telemetry_endpoint: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The telemetry endpoint for the Amazon ECS agent.</p>"""
    service_connect_endpoint: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The endpoint for the Amazon ECS agent to poll for Service Connect configuration. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html\">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
