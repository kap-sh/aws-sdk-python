"""Generated from Smithy shape ``com.amazonaws.ecs#VpcLatticeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.vpc_lattice_configuration

VpcLatticeConfigurations: TypeAlias = list[
    "capo_ecs.types.vpc_lattice_configuration.VpcLatticeConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcLatticeConfigurations) -> list:
    import capo_ecs.types.vpc_lattice_configuration

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.vpc_lattice_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VpcLatticeConfigurations:
    import capo_ecs.types.vpc_lattice_configuration

    out: VpcLatticeConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.vpc_lattice_configuration.deserialize_aws_json_1_1(item)
        )
    return out
