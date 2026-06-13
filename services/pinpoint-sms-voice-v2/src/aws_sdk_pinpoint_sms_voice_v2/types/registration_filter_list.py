"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_filter

RegistrationFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_filter.RegistrationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_filter

    out: RegistrationFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
