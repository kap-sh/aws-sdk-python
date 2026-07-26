"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#FieldPathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.field_path

FieldPathList: TypeAlias = list["capo_pinpoint_sms_voice_v2.types.field_path.FieldPath"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FieldPathList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FieldPathList:
    return list(data)
