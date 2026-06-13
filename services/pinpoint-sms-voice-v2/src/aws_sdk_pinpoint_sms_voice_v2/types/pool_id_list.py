"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PoolIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_id_or_arn

PoolIdList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PoolIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PoolIdList:
    return list(data)
