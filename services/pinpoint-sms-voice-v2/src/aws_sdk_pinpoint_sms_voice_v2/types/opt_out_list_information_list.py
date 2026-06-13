"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OptOutListInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information

OptOutListInformationList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information.OptOutListInformation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptOutListInformationList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OptOutListInformationList:
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information

    out: OptOutListInformationList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_information.deserialize_aws_json_1_0(
                item
            )
        )
    return out
