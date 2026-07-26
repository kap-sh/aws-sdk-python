"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationAttachmentsInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_attachments_information

RegistrationAttachmentsInformationList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.registration_attachments_information.RegistrationAttachmentsInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationAttachmentsInformationList) -> list:
    import capo_pinpoint_sms_voice_v2.types.registration_attachments_information

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_attachments_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationAttachmentsInformationList:
    import capo_pinpoint_sms_voice_v2.types.registration_attachments_information

    out: RegistrationAttachmentsInformationList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_attachments_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
