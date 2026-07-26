"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationAssociationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.registration_association_filter

RegistrationAssociationFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.registration_association_filter.RegistrationAssociationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationAssociationFilterList) -> list:
    import capo_pinpoint_sms_voice_v2.types.registration_association_filter

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_association_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RegistrationAssociationFilterList:
    import capo_pinpoint_sms_voice_v2.types.registration_association_filter

    out: RegistrationAssociationFilterList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.registration_association_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
