"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#KeywordFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter

KeywordFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter.KeywordFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeywordFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> KeywordFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter

    out: KeywordFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.keyword_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
