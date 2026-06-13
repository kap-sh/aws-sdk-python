"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PoolFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_filter

PoolFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.pool_filter.PoolFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PoolFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.pool_filter.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PoolFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.pool_filter

    out: PoolFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.pool_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
