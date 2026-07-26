"""Generated from Smithy shape ``com.amazonaws.gamelift#VpcSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.vpc_subnet

VpcSubnets: TypeAlias = list["capo_gamelift.types.vpc_subnet.VpcSubnet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcSubnets) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcSubnets:
    return list(data)
