"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#KeywordInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.keyword_information

KeywordInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.keyword_information.KeywordInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeywordInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.keyword_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.keyword_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> KeywordInformationList:
    import capo_pinpoint_sms_voice_v2.types.keyword_information

    out: KeywordInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.keyword_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
