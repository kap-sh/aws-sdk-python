"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyAvailabilityZoneGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_availability_zone_opt_in_status
    import aws_sdk_ec2.types.string


class ModifyAvailabilityZoneGroupRequest(TypedDict):
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Availability Zone group, Local Zone group, or Wavelength Zone group.</p>"""
    opt_in_status: NotRequired[
        "aws_sdk_ec2.types.modify_availability_zone_opt_in_status.ModifyAvailabilityZoneOptInStatus"
    ]
    """<p>Indicates whether to opt in to the zone group. The only valid value is <code>opted-in</code>. You must contact Amazon Web Services Support to opt out of a Local Zone or Wavelength Zone group.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
