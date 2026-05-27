"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneSubGeography``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AvailabilityZoneSubGeography(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the sub-geography, for example, <code>Oregon.</code> </p>"""
