"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#KeywordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword

KeywordList: TypeAlias = list["aws_sdk_pinpoint_sms_voice_v2.types.keyword.Keyword"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeywordList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> KeywordList:
    return list(data)
