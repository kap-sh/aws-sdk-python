"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#MonthlySettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.monthly_setting

MonthlySettings: TypeAlias = list[
    "capo_ssm_contacts.types.monthly_setting.MonthlySetting"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonthlySettings) -> list:
    import capo_ssm_contacts.types.monthly_setting

    out: list = []
    for item in value:
        out.append(capo_ssm_contacts.types.monthly_setting.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MonthlySettings:
    import capo_ssm_contacts.types.monthly_setting

    out: MonthlySettings = []
    for item in data:
        out.append(
            capo_ssm_contacts.types.monthly_setting.deserialize_aws_json_1_1(item)
        )
    return out
