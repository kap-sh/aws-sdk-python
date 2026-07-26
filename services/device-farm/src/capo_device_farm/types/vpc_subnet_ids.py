"""Generated from Smithy shape ``com.amazonaws.devicefarm#VpcSubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.subnet_id

VpcSubnetIds: TypeAlias = list["capo_device_farm.types.subnet_id.SubnetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcSubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcSubnetIds:
    return list(data)
