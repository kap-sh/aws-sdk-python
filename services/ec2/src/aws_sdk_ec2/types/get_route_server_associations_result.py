"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_associations_list


class GetRouteServerAssociationsResult(TypedDict):
    route_server_associations: NotRequired[
        "aws_sdk_ec2.types.route_server_associations_list.RouteServerAssociationsList"
    ]
    """<p>Information about the associations for the specified route server.</p>"""
