"""Generated from Smithy shape ``com.amazonaws.ec2#FleetIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_id

FleetIdSet: TypeAlias = list["aws_sdk_ec2.types.fleet_id.FleetId"]
