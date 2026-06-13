"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#DbInstanceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_influxdb.types.db_instance_id

DbInstanceIdList: TypeAlias = list[
    "aws_sdk_timestream_influxdb.types.db_instance_id.DbInstanceId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DbInstanceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> DbInstanceIdList:
    return list(data)
