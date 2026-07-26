"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SenderIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.sender_id_and_country

SenderIdList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.sender_id_and_country.SenderIdAndCountry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderIdList) -> list:
    import capo_pinpoint_sms_voice_v2.types.sender_id_and_country

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.sender_id_and_country.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SenderIdList:
    import capo_pinpoint_sms_voice_v2.types.sender_id_and_country

    out: SenderIdList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.sender_id_and_country.deserialize_aws_json_1_0(
                item
            )
        )
    return out
