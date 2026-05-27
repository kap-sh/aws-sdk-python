"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_data

FleetSet: TypeAlias = list["aws_sdk_ec2.types.fleet_data.FleetData"]
