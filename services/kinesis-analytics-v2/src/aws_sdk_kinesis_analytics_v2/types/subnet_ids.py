"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.subnet_id

SubnetIds: TypeAlias = list["aws_sdk_kinesis_analytics_v2.types.subnet_id.SubnetId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetIds:
    return list(data)
