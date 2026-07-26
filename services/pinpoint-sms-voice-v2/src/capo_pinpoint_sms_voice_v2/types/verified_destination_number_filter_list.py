"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#VerifiedDestinationNumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter

VerifiedDestinationNumberFilterList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter.VerifiedDestinationNumberFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerifiedDestinationNumberFilterList) -> list:
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VerifiedDestinationNumberFilterList:
    import capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter

    out: VerifiedDestinationNumberFilterList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.verified_destination_number_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
