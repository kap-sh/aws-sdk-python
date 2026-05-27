"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneMessage``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AvailabilityZoneMessage(TypedDict):
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The message about the Availability Zone, Local Zone, or Wavelength Zone.</p>"""
