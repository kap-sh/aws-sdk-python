"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialAccountInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.free_trial_account_info

FreeTrialAccountInfoList: TypeAlias = list[
    "capo_inspector2.types.free_trial_account_info.FreeTrialAccountInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialAccountInfoList) -> list:
    import capo_inspector2.types.free_trial_account_info

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.free_trial_account_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> FreeTrialAccountInfoList:
    import capo_inspector2.types.free_trial_account_info

    out: FreeTrialAccountInfoList = []
    for item in data:
        out.append(capo_inspector2.types.free_trial_account_info.deserialize_json(item))
    return out
