"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEndpointsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item_set


class DeleteVpcEndpointsResult(TypedDict):
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the VPC endpoints that were not successfully deleted.</p>"""
