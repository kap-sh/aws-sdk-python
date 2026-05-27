"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateServiceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service


class UpdateServiceResponse(TypedDict):
    service: NotRequired["aws_sdk_ecs.types.service.Service"]
    """<p>The full description of your service following the update call.</p> <p>The response includes a <code>lifecycleHookDetails</code> field, which is an empty array when the service is created or updated. The values are populated when a lifecycle hook executes and are available as part of the service deployment details (<a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html\">DescribeServiceDeployments</a>).</p>"""
