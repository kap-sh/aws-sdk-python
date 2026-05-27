"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotFleetResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class RequestSpotFleetResponse(TypedDict):
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""
