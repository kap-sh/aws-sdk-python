"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetRequestConfigSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_fleet_request_config

SpotFleetRequestConfigSet: TypeAlias = list[
    "aws_sdk_ec2.types.spot_fleet_request_config.SpotFleetRequestConfig"
]
