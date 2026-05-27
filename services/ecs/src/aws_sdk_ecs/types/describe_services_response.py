"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServicesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.services


class DescribeServicesResponse(TypedDict):
    services: NotRequired["aws_sdk_ecs.types.services.Services"]
    """<p>The list of services described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""
