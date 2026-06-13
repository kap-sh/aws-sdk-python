"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OptedOutFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.opted_out_filter

OptedOutFilterList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.opted_out_filter.OptedOutFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptedOutFilterList) -> list:
    import aws_sdk_pinpoint_sms_voice_v2.types.opted_out_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.opted_out_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OptedOutFilterList:
    import aws_sdk_pinpoint_sms_voice_v2.types.opted_out_filter

    out: OptedOutFilterList = []
    for item in data:
        out.append(
            aws_sdk_pinpoint_sms_voice_v2.types.opted_out_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
