"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_fleet_request_id

SpotFleetRequestIdList: TypeAlias = list[
    "aws_sdk_ec2.types.spot_fleet_request_id.SpotFleetRequestId"
]
