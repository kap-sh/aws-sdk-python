"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#VpcSecurityGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.vpc_security_group_id

VpcSecurityGroupIdList: TypeAlias = list[
    "capo_timestream_influxdb.types.vpc_security_group_id.VpcSecurityGroupId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcSecurityGroupIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VpcSecurityGroupIdList:
    return list(data)
