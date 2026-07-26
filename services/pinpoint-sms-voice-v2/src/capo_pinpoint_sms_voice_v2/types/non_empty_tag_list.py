"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NonEmptyTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.tag

NonEmptyTagList: TypeAlias = list["capo_pinpoint_sms_voice_v2.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NonEmptyTagList) -> list:
    import capo_pinpoint_sms_voice_v2.types.tag

    out: list = []
    for item in value:
        out.append(capo_pinpoint_sms_voice_v2.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> NonEmptyTagList:
    import capo_pinpoint_sms_voice_v2.types.tag

    out: NonEmptyTagList = []
    for item in data:
        out.append(capo_pinpoint_sms_voice_v2.types.tag.deserialize_aws_json_1_0(item))
    return out
