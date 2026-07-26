"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyTemplateIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.notify_template_id

NotifyTemplateIdList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.notify_template_id.NotifyTemplateId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyTemplateIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NotifyTemplateIdList:
    return list(data)
