"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerOrganizationsAccessResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_status


class UpdateCapacityManagerOrganizationsAccessResult(TypedDict):
    capacity_manager_status: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_status.CapacityManagerStatus"
    ]
    """<p> The current status of Capacity Manager after the update operation. </p>"""
    organizations_access: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> The updated Organizations access setting indicating whether cross-account data aggregation is enabled. </p>"""
