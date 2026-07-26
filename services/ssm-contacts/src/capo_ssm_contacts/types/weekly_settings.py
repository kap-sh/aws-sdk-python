"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#WeeklySettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.weekly_setting

WeeklySettings: TypeAlias = list["capo_ssm_contacts.types.weekly_setting.WeeklySetting"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WeeklySettings) -> list:
    import capo_ssm_contacts.types.weekly_setting

    out: list = []
    for item in value:
        out.append(capo_ssm_contacts.types.weekly_setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WeeklySettings:
    import capo_ssm_contacts.types.weekly_setting

    out: WeeklySettings = []
    for item in data:
        out.append(
            capo_ssm_contacts.types.weekly_setting.deserialize_aws_json_1_1(item)
        )
    return out
