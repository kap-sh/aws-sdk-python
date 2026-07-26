"""Generated from Smithy shape ``com.amazonaws.devicefarm#VpcSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.security_group_id

VpcSecurityGroupIds: TypeAlias = list[
    "capo_device_farm.types.security_group_id.SecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VpcSecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> VpcSecurityGroupIds:
    return list(data)
