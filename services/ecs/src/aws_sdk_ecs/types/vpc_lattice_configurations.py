"""Generated from Smithy shape ``com.amazonaws.ecs#VpcLatticeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.vpc_lattice_configuration

VpcLatticeConfigurations: TypeAlias = list[
    "aws_sdk_ecs.types.vpc_lattice_configuration.VpcLatticeConfiguration"
]
