"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NotifyTemplateInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information

NotifyTemplateInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information.NotifyTemplateInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NotifyTemplateInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NotifyTemplateInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information

    out: NotifyTemplateInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.notify_template_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
