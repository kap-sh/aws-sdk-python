"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationVersionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_filter

RegistrationVersionFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.registration_version_filter.RegistrationVersionFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationVersionFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_version_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationVersionFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_version_filter

    out: RegistrationVersionFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.registration_version_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
