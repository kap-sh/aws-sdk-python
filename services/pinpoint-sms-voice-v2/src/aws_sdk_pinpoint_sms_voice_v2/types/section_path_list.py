"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SectionPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.section_path

SectionPathList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.section_path.SectionPath"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SectionPathList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SectionPathList:
    return list(data)
