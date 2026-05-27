"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table
    import aws_sdk_ec2.types.string


class CreateRouteTableResult(TypedDict):
    route_table: NotRequired["aws_sdk_ec2.types.route_table.RouteTable"]
    """<p>Information about the route table.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""
