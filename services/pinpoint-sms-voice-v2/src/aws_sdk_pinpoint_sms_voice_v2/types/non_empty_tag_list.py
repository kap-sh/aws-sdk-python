"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NonEmptyTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.tag

NonEmptyTagList: TypeAlias = list["aws_sdk_pinpoint_sms_voice_v2.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NonEmptyTagList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint_sms_voice_v2.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> NonEmptyTagList:
    import aws_sdk_pinpoint_sms_voice_v2.types.tag

    out: NonEmptyTagList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.tag.deserialize_aws_json_1_0(item)
        )
    return out
