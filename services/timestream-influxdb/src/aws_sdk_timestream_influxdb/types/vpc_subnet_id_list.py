"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#VpcSubnetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.vpc_subnet_id

VpcSubnetIdList: TypeAlias = list[
    "aws_sdk_timestream_influxdb.types.vpc_subnet_id.VpcSubnetId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcSubnetIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VpcSubnetIdList:
    return list(data)
