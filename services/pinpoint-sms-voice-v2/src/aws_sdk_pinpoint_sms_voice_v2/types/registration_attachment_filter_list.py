"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationAttachmentFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_filter

RegistrationAttachmentFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_filter.RegistrationAttachmentFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationAttachmentFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationAttachmentFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_filter

    out: RegistrationAttachmentFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
