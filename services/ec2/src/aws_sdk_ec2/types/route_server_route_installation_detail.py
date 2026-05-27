"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRouteInstallationDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_route_installation_status
    import aws_sdk_ec2.types.route_table_id
    import aws_sdk_ec2.types.string


class RouteServerRouteInstallationDetail(TypedDict):
    route_table_id: NotRequired["aws_sdk_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the route table where the route is being installed.</p>"""
    route_installation_status: NotRequired[
        "aws_sdk_ec2.types.route_server_route_installation_status.RouteServerRouteInstallationStatus"
    ]
    """<p>The current installation status of the route in the route table.</p>"""
    route_installation_status_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current installation status of the route.</p>"""
