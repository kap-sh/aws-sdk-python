"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceNetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class ExpressGatewayServiceNetworkConfiguration(TypedDict):
    security_groups: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The IDs of the security groups associated with the Express service.</p>"""
    subnets: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The IDs of the subnets associated with the Express service.</p>"""
