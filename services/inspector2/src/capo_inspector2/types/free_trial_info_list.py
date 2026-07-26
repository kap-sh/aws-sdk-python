"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.free_trial_info

FreeTrialInfoList: TypeAlias = list[
    "capo_inspector2.types.free_trial_info.FreeTrialInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialInfoList) -> list:
    import capo_inspector2.types.free_trial_info

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.free_trial_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> FreeTrialInfoList:
    import capo_inspector2.types.free_trial_info

    out: FreeTrialInfoList = []
    for item in data:
        out.append(capo_inspector2.types.free_trial_info.deserialize_json(item))
    return out
