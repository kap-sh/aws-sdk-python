"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#VoiceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.voice_id

VoiceIdList: TypeAlias = list["capo_pinpoint_sms_voice_v2.types.voice_id.VoiceId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VoiceIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VoiceIdList:
    return list(data)
