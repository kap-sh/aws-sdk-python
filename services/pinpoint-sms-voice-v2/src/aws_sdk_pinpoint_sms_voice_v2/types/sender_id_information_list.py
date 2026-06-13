"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SenderIdInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information

SenderIdInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information.SenderIdInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderIdInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SenderIdInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information

    out: SenderIdInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.sender_id_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
