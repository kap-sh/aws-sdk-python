"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AccountAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_attribute

AccountAttributeList: TypeAlias = list["aws_sdk_pinpoint_sms_voice_v2.types.account_attribute.AccountAttribute"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountAttributeList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_attribute
    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint_sms_voice_v2.types.account_attribute.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> AccountAttributeList:
    import aws_sdk_pinpoint_sms_voice_v2.types.account_attribute
    out: AccountAttributeList = []
    for item in data:
        out.append(aws_sdk_pinpoint_sms_voice_v2.types.account_attribute.deserialize_aws_json_1_0(item))
    return out