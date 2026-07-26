"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SenderIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.sender_id_filter

SenderIdFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.sender_id_filter.SenderIdFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderIdFilterList) -> list:
    import capo_pinpoint_sms_voice_v2.types.sender_id_filter

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.sender_id_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SenderIdFilterList:
    import capo_pinpoint_sms_voice_v2.types.sender_id_filter

    out: SenderIdFilterList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.sender_id_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
