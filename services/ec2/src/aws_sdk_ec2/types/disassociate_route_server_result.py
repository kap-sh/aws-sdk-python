"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateRouteServerResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_association


class DisassociateRouteServerResult(TypedDict):
    route_server_association: NotRequired[
        "aws_sdk_ec2.types.route_server_association.RouteServerAssociation"
    ]
    """<p>Information about the disassociated route server.</p>"""
