"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccountLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_limit

AccountLimitList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.account_limit.AccountLimit"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountLimitList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_limit

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.account_limit.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AccountLimitList:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_limit

    out: AccountLimitList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.account_limit.deserialize_aws_json_1_0(
                item
            )
        )
    return out
