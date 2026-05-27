"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorManufacturerSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.accelerator_manufacturer

AcceleratorManufacturerSet: TypeAlias = list[
    "aws_sdk_ecs.types.accelerator_manufacturer.AcceleratorManufacturer"
]
