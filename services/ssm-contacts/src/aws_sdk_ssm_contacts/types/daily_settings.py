"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DailySettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.hand_off_time

DailySettings: TypeAlias = list["aws_sdk_ssm_contacts.types.hand_off_time.HandOffTime"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DailySettings) -> list:
    import aws_sdk_ssm_contacts.types.hand_off_time

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.hand_off_time.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DailySettings:
    import aws_sdk_ssm_contacts.types.hand_off_time

    out: DailySettings = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.hand_off_time.deserialize_aws_json_1_1(item)
        )
    return out
