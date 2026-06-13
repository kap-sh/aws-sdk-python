"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#VerifiedDestinationNumberIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn

VerifiedDestinationNumberIdList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.verified_destination_number_id_or_arn.VerifiedDestinationNumberIdOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerifiedDestinationNumberIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VerifiedDestinationNumberIdList:
    return list(data)
