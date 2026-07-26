"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyTemplateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.notify_template_filter

NotifyTemplateFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.notify_template_filter.NotifyTemplateFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyTemplateFilterList) -> list:
    import capo_pinpoint_sms_voice_v2.types.notify_template_filter

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.notify_template_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NotifyTemplateFilterList:
    import capo_pinpoint_sms_voice_v2.types.notify_template_filter

    out: NotifyTemplateFilterList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.notify_template_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
