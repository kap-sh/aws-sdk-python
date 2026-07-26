"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#DailySettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.hand_off_time

DailySettings: TypeAlias = list["capo_ssm_contacts.types.hand_off_time.HandOffTime"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DailySettings) -> list:
    import capo_ssm_contacts.types.hand_off_time

    out: list = []
    for item in value:
        out.append(capo_ssm_contacts.types.hand_off_time.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DailySettings:
    import capo_ssm_contacts.types.hand_off_time

    out: DailySettings = []
    for item in data:
        out.append(capo_ssm_contacts.types.hand_off_time.deserialize_aws_json_1_1(item))
    return out
