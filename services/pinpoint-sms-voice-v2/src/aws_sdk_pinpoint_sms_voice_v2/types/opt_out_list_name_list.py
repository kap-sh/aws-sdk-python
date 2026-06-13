"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OptOutListNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn

OptOutListNameList: TypeAlias = list[
    "aws_sdk_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptOutListNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> OptOutListNameList:
    return list(data)
