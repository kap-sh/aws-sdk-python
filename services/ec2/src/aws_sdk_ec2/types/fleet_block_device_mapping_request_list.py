"""Generated from Smithy shape ``com.amazonaws.ec2#FleetBlockDeviceMappingRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_block_device_mapping_request

FleetBlockDeviceMappingRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_block_device_mapping_request.FleetBlockDeviceMappingRequest"
]
