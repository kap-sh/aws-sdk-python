"""Generated from Smithy shape ``com.amazonaws.ec2#CpuManufacturerSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cpu_manufacturer

CpuManufacturerSet: TypeAlias = list[
    "aws_sdk_ec2.types.cpu_manufacturer.CpuManufacturer"
]
