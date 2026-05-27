"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEndpointServiceConfigurationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.unsuccessful_item_set


class DeleteVpcEndpointServiceConfigurationsResult(TypedDict):
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.unsuccessful_item_set.UnsuccessfulItemSet"
    ]
    """<p>Information about the service configurations that were not deleted, if applicable.</p>"""
