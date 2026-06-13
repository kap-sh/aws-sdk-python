"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#PhoneNumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number_filter

PhoneNumberFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.phone_number_filter.PhoneNumberFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PhoneNumberFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.phone_number_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PhoneNumberFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.phone_number_filter

    out: PhoneNumberFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.phone_number_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
