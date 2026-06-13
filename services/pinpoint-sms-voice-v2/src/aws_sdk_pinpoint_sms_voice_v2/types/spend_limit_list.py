"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SpendLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.spend_limit

SpendLimitList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.spend_limit.SpendLimit"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpendLimitList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.spend_limit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.spend_limit.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SpendLimitList:
    import aws_sdk_pinpoint_sms_voice_v2.types.spend_limit

    out: SpendLimitList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.spend_limit.deserialize_aws_json_1_0(
                item
            )
        )
    return out
