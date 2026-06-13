"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationAttachmentsInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_attachments_information

RegistrationAttachmentsInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_attachments_information.RegistrationAttachmentsInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationAttachmentsInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_attachments_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_attachments_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationAttachmentsInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_attachments_information

    out: RegistrationAttachmentsInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_attachments_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
