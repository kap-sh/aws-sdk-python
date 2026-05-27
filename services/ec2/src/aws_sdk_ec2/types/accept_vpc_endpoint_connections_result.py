"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcEndpointConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item_set


class AcceptVpcEndpointConnectionsResult(TypedDict):
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the interface endpoints that were not accepted, if applicable.</p>"""
