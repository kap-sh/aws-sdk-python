"""Generated from Smithy shape ``com.amazonaws.guardduty#AccountFreeTrialInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.account_free_trial_info

AccountFreeTrialInfos: TypeAlias = list[
    "capo_guardduty.types.account_free_trial_info.AccountFreeTrialInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountFreeTrialInfos) -> list:
    import capo_guardduty.types.account_free_trial_info

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.account_free_trial_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccountFreeTrialInfos:
    import capo_guardduty.types.account_free_trial_info

    out: AccountFreeTrialInfos = []
    for item in data:
        out.append(capo_guardduty.types.account_free_trial_info.deserialize_json(item))
    return out
