"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_fleet_error_set
    import aws_sdk_ec2.types.delete_fleet_success_set


class DeleteFleetsResult(TypedDict):
    successful_fleet_deletions: NotRequired[
        "aws_sdk_ec2.types.delete_fleet_success_set.DeleteFleetSuccessSet"
    ]
    """<p>Information about the EC2 Fleets that are successfully deleted.</p>"""
    unsuccessful_fleet_deletions: NotRequired[
        "aws_sdk_ec2.types.delete_fleet_error_set.DeleteFleetErrorSet"
    ]
    """<p>Information about the EC2 Fleets that are not successfully deleted.</p>"""
